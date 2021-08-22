#!/bin/python

# https://cryptopals.com/sets/1/challenges/7

from Crypto.Cipher import AES
from base64 import b64decode

def aes_128_ecb_decrypt(ciphertext, key):
    # Decode the ciphertext (it's encoded in base64)
    data = b64decode(ciphertext)
    cipher = AES.new(key.encode("utf8"), AES.MODE_ECB)
    result = cipher.decrypt(data).decode()
    return result



if __name__ == "__main__":
    key = "YELLOW SUBMARINE"
    with open("7.txt", "r") as f:
        ciphertext = f.read()

    print(aes_128_ecb_decrypt(ciphertext, key))
