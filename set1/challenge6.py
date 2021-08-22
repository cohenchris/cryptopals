#!/bin/python
# https://cryptopals.com/sets/1/challenges/6

from __future__ import division
from base64 import b64decode
import sys

from challenge1 import hex_to_binary

MAXKEYSIZE = 40

def ascii_to_binary(string):
    binary_str = ""
    for char in string:
        binary_str = binary_str + bin(ord(char))[2:].zfill(8)

    return binary_str



def compute_hamming_distance(str1, str2):
    assert len(str1) == len(str2)

    # Convert each string to binary
    s1 = ascii_to_binary(str1.decode())
    s2 = ascii_to_binary(str2.decode())

    hamming = 0
    [hamming := hamming + 1 for i in range(len(s1)) if s1[i] != s2[i]]

    return hamming



def find_key_candidates(content):
    candidates = {}
    for i in range(2, MAXKEYSIZE):
        KEYSIZE = i
        first_n_bytes = content[:KEYSIZE]
        second_n_bytes = content[KEYSIZE:KEYSIZE*2]

        diff = compute_hamming_distance(first_n_bytes, second_n_bytes)
        candidates[KEYSIZE] = diff/KEYSIZE

    return sorted(candidates, key=lambda c: candidates[c])[:3]



def break_repeating_key_xor(filename):
    content = ""
    with open(filename, "r") as f:
        content = b64decode(f.read())

    key_candidates = find_key_candidates(content)

    for key in key_candidates:
        # Break ciphertext into blocks of 'key' length
        for i in range(key):
            # Transpose blocks
            for j in range(i, len(content), key):
                block = block + bytes(
                # TODO ...







str1 = b'this is a test'
str2 = b'wokka wokka!!!'
if __name__ == "__main__":
    assert compute_hamming_distance(str1, str2) == 37

    break_repeating_key_xor("6.txt")
