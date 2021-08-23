#!/bin/python

# https://cryptopals.com/sets/1/challenges/2

from challenge1 import hex_to_binary

def hex_xor(hex1, hex2):
    xor = int(hex1, 16) ^ int(hex2, 16)
    return hex(xor)[2:].encode()


str1 = b'1c0111001f010100061a024b53535009181c'
str2 = b'686974207468652062756c6c277320657965'
solution = b'746865206b696420646f6e277420706c6179'

if __name__ == "__main__":
    assert hex_xor(str1, str2) == solution
