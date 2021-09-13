#!/bin/python

# https://cryptopals.com/sets/2/challenges/11

import random
from Crypto.Cipher import AES

from challenge10 import aes_128_ecb_encrypt, cbc_encrypt
from challenge8 import count_repeated_chunks

AES_KEYSIZE = 16
BLOCKSIZE = AES.block_size

def aes_keygen():
    return random.randbytes(AES_KEYSIZE)

def encryption_oracle(plaintext):
    """
        Take in a plaintext block and add 5-10 random bytes
        at the beginning and end. Encrypt using an unknown key,
        using ECB 1/2 of the time and CBC the other 1/2.
    """
    # Randomly prepend/append 5-10 bytes to the plaintext
    prepend = random.randbytes(random.randint(5, 10))
    append = random.randbytes(random.randint(5, 10))
    plaintext = prepend + plaintext + append


    key = aes_keygen()

    choice =  random.randrange(2)
    if choice:
        # ECB
        return aes_128_ecb_encrypt(plaintext, key)
        pass
    else:
        # CBC
        iv = random.randbytes(BLOCKSIZE)
        return cbc_encrypt(plaintext, key, iv)
        pass


def cbc_or_ecb(ciphertext):
    repeats = count_repeated_chunks(ciphertext)["repeated_chunks"]

    if repeats > 0:
        return "ecb"
    else:
        return "cbc"

if __name__ == "__main__":
    pt = b'yeet dab yolo swag ayyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy'
    cbc_or_ecb(encryption_oracle(pt))
