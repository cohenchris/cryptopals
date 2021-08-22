#!/bin/python

# https://cryptopals.com/sets/1/challenges/3

from challenge1 import hex_to_binary
from challenge2 import hex_xor

# https://gist.github.com/pozhidaevak/0dca594d6f0de367f232909fe21cdb2f
letterFrequency = {'E' : 12.0,
        'T' : 9.10,
        'A' : 8.12,
        'O' : 7.68,
        'I' : 7.31,
        'N' : 6.95,
        'S' : 6.28,
        'R' : 6.02,
        'H' : 5.92,
        'D' : 4.32,
        'L' : 3.98,
        'U' : 2.88,
        'C' : 2.71,
        'M' : 2.61,
        'F' : 2.30,
        'Y' : 2.11,
        'W' : 2.09,
        'G' : 2.03,
        'P' : 1.82,
        'B' : 1.49,
        'V' : 1.11,
        'K' : 0.69,
        'X' : 0.17,
        'Q' : 0.11,
        'J' : 0.10,
        'Z' : 0.07,
        ' ' : 19 }

def score_string(string):
    score = 0
    for char in string:
        try:
            score = score + letterFrequency[char.upper()]
        except KeyError:
            continue

    return score



def hex_to_ascii(hex_val):
    ascii_str = ""
    for i in range(0, len(hex_val), 2):
        ascii_str = ascii_str + chr(int(hex_val[i:i+2], 16))

    return ascii_str



def single_byte_xor(hex_val, byte):
    result = b''
    for i in range(0, len(hex_val), 2):
        result += hex_xor(hex_val[i:i+2], hex(byte)[2:].zfill(2))

    result = hex_to_ascii(result)
    return result



def decrypt_string_xored_by_single_char(hex_str):
    plaintext_candidates = {}
    for i in range(256):
        plaintext_candidates[i] = single_byte_xor(hex_str, i)

    key = max(plaintext_candidates, key=lambda c: score_string(plaintext_candidates[c]))

    return {"key": key, "plaintext": plaintext_candidates[key]}


hex_str = b'1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'

if __name__ == "__main__":
    assert decrypt_string_xored_by_single_char(hex_str)["plaintext"] == "Cooking MC's like a pound of bacon"
