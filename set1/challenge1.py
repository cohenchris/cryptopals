#!/bin/python

# https://cryptopals.com/sets/1/challenges/1

b64_table = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"


def hex_to_binary(hex_val):
    # Convert hex to binary
    i = 0
    binary_str = b''
    for i in range(0, len(hex_val), 2):
        byte = hex_val[i:i+2]
        binary = bin(int(byte, 16))[2:].zfill(8).encode()
        binary_str += binary

    return binary_str


def binary_to_b64(binary):
    i = 0
    b64 = b''
    for i in range(0, len(binary), 6):
        group = binary[i:i+6]
        b64 +=  b64_table[int(group, 2)].encode()

    return b64


def hex_to_b64(hex_string):
    return(binary_to_b64(hex_to_binary(hex_string)))



hex_string = b'49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d'
solution = b'SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t'

if __name__ == "__main__":
    assert hex_to_b64(hex_string) == solution
