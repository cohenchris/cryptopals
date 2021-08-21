#!/bin/python

# https://cryptopals.com/sets/1/challenges/1

b64_table = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"


def hex_to_binary(hex_str):
    # Convert hex string to binary
    i = 0
    binary_str = ""
    while i < len(hex_str) - 1:
        byte = hex_str[i:i+2]
        binary = bin(int(byte, 16))[2:].zfill(8)
        binary_str = binary_str + binary
        i = i + 2

    return binary_str


def binary_to_b64(binary_str):
    # Convert binary string to base 64
    hex_byte_arr = bytearray.fromhex(binary_str)
    i = 0
    b64_str = ""
    while i < len(binary_str) - 1:
        group = binary_str[i:i+6]
        b64_str = b64_str + b64_table[int(group, 2)]
        i = i + 6

    return b64_str


def hex_to_b64(hex_string):
    return(binary_to_b64(hex_to_binary(hex_string)))



hex_string = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"
solution = "SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t"

if __name__ == "__main__":
    assert hex_to_b64(hex_string) == solution

