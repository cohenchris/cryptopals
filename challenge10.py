#!/bin/python

# https://cryptopals.com/sets/2/challenges/10

from base64 import b64decode
from Crypto.Cipher import AES
from pprint import pprint

from challenge2 import hex_xor
from challenge7 import aes_128_ecb_decrypt
from challenge9 import pkcs7_pad, pkcs7_unpad

BLOCKSIZE = AES.block_size

# https://stackoverflow.com/questions/23312571/fast-xoring-bytes-in-python-3
def xor_bytes(b1, b2):
    parts = []
    for b1, b2 in zip(b1, b2):
        parts.append(bytes([b1 ^ b2]))
    return b''.join(parts)
        


def aes_128_ecb_encrypt(plaintext, key):
    cipher = AES.new(key, AES.MODE_ECB)
    result = cipher.encrypt(pkcs7_pad(plaintext, BLOCKSIZE))
    return result


def cbc_decrypt(ciphertext, key, iv):
    blocks = [ciphertext[i:i+BLOCKSIZE] for i in range(0, len(ciphertext), BLOCKSIZE)]

    decrypted = b''
    working_block = b''

    for i, block in enumerate(blocks):
        working_block = aes_128_ecb_decrypt(block, key)

        if i == 0:
            working_block = xor_bytes(iv, working_block)
        else:
            working_block = xor_bytes(blocks[i-1], working_block)

        decrypted += working_block

    return pkcs7_unpad(decrypted, BLOCKSIZE)


def cbc_encrypt(plaintext, key, iv):
    # Split plaintext into BLOCKSIZE blocks (padded if needed)
    blocks = [pkcs7_pad(plaintext[i:i+BLOCKSIZE], BLOCKSIZE) for i in range(0, len(plaintext), BLOCKSIZE)]

    encrypted = b''
    working_block = b''

    for i, block in enumerate(blocks):
        if i == 0:
            # if first block, XOR with IV
            working_block = xor_bytes(iv, block)
        else:
            working_block = xor_bytes(working_block, block)

        working_block = aes_128_ecb_encrypt(working_block, key)
        encrypted += working_block

    return encrypted


if __name__ == "__main__":
    # Test basic encryption/decryption
    test_str = b'There are over 500 starfish in the bathroom drawer. The snow-covered path was no help in finding his way out of the back-country. I was fishing for compliments and accidentally caught a trout. As he entered the church he could hear the soft voice of someone whispering into a cell phone.'
    key = b'YELLOW SUBMARINE'
    encrypted = aes_128_ecb_encrypt(test_str, key)
    decrypted = aes_128_ecb_decrypt(encrypted, key)
    assert decrypted == test_str

    # CBC
    iv = b'\x00' * BLOCKSIZE

    with open("10.txt", "r") as f:
        ciphertext = b64decode(f.read())

    print(cbc_decrypt(ciphertext, key, iv).decode())

    assert cbc_decrypt(cbc_encrypt(test_str, key, iv), key, iv) == test_str
