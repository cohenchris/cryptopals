#!/bin/python
# https://cryptopals.com/sets/1/challenges/6

from __future__ import division
from base64 import b64decode
import sys
from pprint import pprint

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



def find_key_candidates(content):
    candidates = {}
    for i in range(2, MAXKEYSIZE):
        KEYSIZE = i
        first_n_bytes = content[:KEYSIZE]
        second_n_bytes = content[KEYSIZE:KEYSIZE*2]

        diff = compute_hamming_distance(first_n_bytes, second_n_bytes)
        candidates[KEYSIZE] = diff/KEYSIZE

    return sorted(candidates, key=lambda c: candidates[c])[:3]



def break_repeating_key_xor(data):
    key_candidates = find_key_candidates(data)

    possible_plaintexts = []

    for candidate in key_candidates:
        key = b''
        blocks = []


        # Break ciphertext into blocks of 'candidate' length
        for i in range(candidate):
            block = b''

            # Transpose blocks into blocks of the i-th byte of each block
            for j in range(i, len(data), candidate):
                block += bytes([data[j]])
    
            blocks.append(block)


        # Brute-force solve each block
        for block in blocks:
            key += bytes([decrypt_string_xored_by_single_char(block.hex())["key"]])

        # todo
        
        temp = repeating_key_xor(data, key).decode()
        bytes_obj = bytes.fromhex(temp)
        ascii_str = bytes_obj.decode("ASCII")
        possible_plaintexts.append(ascii_str)

    pprint(possible_plaintexts)

    return max(possible_plaintexts, key=score_string)





str1 = b'this is a test'
str2 = b'wokka wokka!!!'
if __name__ == "__main__":
    assert compute_hamming_distance(str1, str2) == 37

    with open("6.txt", "r") as f:
        content = b64decode(f.read())

    break_repeating_key_xor(content)
