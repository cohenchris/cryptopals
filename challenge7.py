#!/bin/python

# https://cryptopals.com/sets/1/challenges/7

from Crypto.Cipher import AES
from base64 import b64decode
from challenge9 import pkcs7_unpad

def aes_128_ecb_decrypt(ciphertext, key):
    # Decode the ciphertext (it's encoded in base64)
    cipher = AES.new(key, AES.MODE_ECB)
    result = cipher.decrypt(ciphertext)
    result = pkcs7_unpad(result, AES.block_size)
    return result


if __name__ == "__main__":
    key = b"YELLOW SUBMARINE"
    with open("7.txt", "r") as f:
        ciphertext = b64decode(f.read())


    print(aes_128_ecb_decrypt(ciphertext, key).decode())
