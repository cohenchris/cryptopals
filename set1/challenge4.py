#!/bin/python

# https://cryptopals.com/sets/1/challenges/4

from challenge3 import brute_force_decrypt, score_string

def decrypt_file(filename):
    with open(filename, "r") as f:
        lines = f.readlines()

    candidates = [brute_force_decrypt(line.strip()) for line in lines]

    return max(candidates, key=score_string)


if __name__ == "__main__":
    assert decrypt_file("4.txt") == "Now that the party is jumping\n"
