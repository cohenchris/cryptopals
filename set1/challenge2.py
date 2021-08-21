#!/bin/python

# https://cryptopals.com/sets/1/challenges/2

from challenge1 import hex_to_binary


def compute_xor(str1, str2):
    assert len(str1) == len(str2)

    binary_str1 = hex_to_binary(str1)
    binary_str2 = hex_to_binary(str2)
    xor_str = ""

    for i in range(len(binary_str1)):
        xor_str = xor_str + str((int(binary_str1[i], 2) ^ int(binary_str2[i], 2)))

    return hex(int(xor_str, 2))[2:]


str1 = "1c0111001f010100061a024b53535009181c"
str2 = "686974207468652062756c6c277320657965"
solution = "746865206b696420646f6e277420706c6179"

if __name__ == "__main__":
    assert compute_xor(str1, str2) == solution
