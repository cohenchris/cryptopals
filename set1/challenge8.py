#!/bin/python

# https://cryptopals.com/sets/1/challenges/8

from Crypto.Cipher.AES import block_size
from pprint import pprint

def count_repeated_chunks(ciphertext):
    # Since ECB is deterministic, there will almost certainly be repeated chunks (for repeated letters)
    BLOCKSIZE = block_size

    # Break into blocks of size BLOCKSIZE
    blocks = [ciphertext[i:i+BLOCKSIZE] for i in range(0, len(ciphertext), BLOCKSIZE)]

    return {"ciphertext": ciphertext, "repeated_chunks": len(blocks) - len(set(blocks))}



def find_ecb_encrypted(ciphertexts):
    repeated_chunks = [count_repeated_chunks(ciphertext) for ciphertext in ciphertexts]

    return max(repeated_chunks, key=lambda c: c["repeated_chunks"])["ciphertext"]
        



SOLUTION = bytes.fromhex("d880619740a8a19b7840a8a31c810a3d08649af70dc06f4fd5d2d69c744cd283e2dd052f6b641dbf9d11b0348542bb5708649af70dc06f4fd5d2d69c744cd2839475c9dfdbc1d46597949d9c7e82bf5a08649af70dc06f4fd5d2d69c744cd28397a93eab8d6aecd566489154789a6b0308649af70dc06f4fd5d2d69c744cd283d403180c98c8f6db1f2a3f9c4040deb0ab51b29933f2c123c58386b06fba186a")


if __name__ == "__main__":
    with open("8.txt", "r") as f:
        ciphertexts = [bytes.fromhex(line.strip()) for line in f]

    assert find_ecb_encrypted(ciphertexts) == SOLUTION
