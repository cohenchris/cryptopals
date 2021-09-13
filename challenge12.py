#!/bin/python

from base64 import b64decode
from pprint import pprint
import string
import math

from challenge10 import aes_128_ecb_encrypt
from challenge11 import cbc_or_ecb

STATIC_KEY = b'Michelangelooooo'

extended_ascii = [chr(i) for i in range(256)]

def encryption_oracle(plaintext):
    append_me = b64decode("Um9sbGluJyBpbiBteSA1LjAKV2l0aCBteSByYWctdG9wIGRvd24gc28gbXkgaGFpciBjYW4gYmxvdwpUaGUgZ2lybGllcyBvbiBzdGFuZGJ5IHdhdmluZyBqdXN0IHRvIHNheSBoaQpEaWQgeW91IHN0b3A/IE5vLCBJIGp1c3QgZHJvdmUgYnkK")
    plaintext = plaintext + append_me

    return aes_128_ecb_encrypt(plaintext, STATIC_KEY)

def find_blocksize():
    i = 1
    last = len(encryption_oracle(b'A' * i))
    i = i + 1

    # Find the length of the plaintext that completes a block

    while True:
        curr = len(encryption_oracle(b'A' * i))
        if curr != last:
            break
        i = i + 1

    return curr - last

def break_oracle():
    mystery_text_len = len(encryption_oracle(b''))

    # Find blocksize
    blocksize = find_blocksize()

    # Check that we are dealing with ECB
    if (cbc_or_ecb(encryption_oracle(b'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'))) != "ecb":
        return False

    BROKEN_STRING = b''
    blocks_found= 0

    for x in range(mystery_text_len):
        partial_input_block = b'A' * ((blocksize - (1 + len(BROKEN_STRING))) % blocksize)

        start = blocks_found * blocksize
        end = start + blocksize

        looking_for = encryption_oracle(partial_input_block)[start:end]

        for i in range(256):
            input_block = partial_input_block + BROKEN_STRING + bytes([i])
            ret = encryption_oracle(input_block)[start:end]
            if ret == looking_for:
                BROKEN_STRING += bytes([i])
                break

        blocks_found = math.floor(len(BROKEN_STRING) / 16)

    return BROKEN_STRING

    

if __name__ == "__main__":
    print(break_oracle().decode())
