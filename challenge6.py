#!/bin/python

# https://cryptopals.com/sets/1/challenges/6

from __future__ import division
from base64 import b64decode
import sys
from itertools import combinations

from challenge1 import hex_to_binary
from challenge3 import decrypt_string_xored_by_single_char, score_string, hex_to_ascii
from challenge5 import repeating_key_xor

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



def find_key(data):
    candidates = {}
    for i in range(2, MAXKEYSIZE):
        first_n_bytes = content[:i]
        second_n_bytes = content[i:i*2]

        chunks = [data[j:j + i] for j in range(0, len(data), i)][:4]
        distance = 0
        pairs = combinations(chunks, 2)
        for (x, y) in pairs:
            distance += compute_hamming_distance(x, y)
        distance /= (6 * i)

        candidates[i] = distance

    return min(candidates, key=lambda c: candidates[c])



def break_repeating_key_xor(data):
    keysize = find_key(data)

    # Try decrypting the ciphertext given keysize
    key = b''

    for i in range(keysize):
        block = b''
        for j in range(i, len(data), keysize):
            block += bytes([data[j]])

        key += bytes([decrypt_string_xored_by_single_char(block)["key"]])

    temp = repeating_key_xor(data, key).decode()
    plaintext = hex_to_ascii(temp)

    return plaintext





str1 = b'this is a test'
str2 = b'wokka wokka!!!'
if __name__ == "__main__":
    assert compute_hamming_distance(str1, str2) == 37

    with open("6.txt", "r") as f:
        content = b64decode(f.read())

    break_repeating_key_xor(content)
