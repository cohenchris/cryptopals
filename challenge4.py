#!/bin/python

# https://cryptopals.com/sets/1/challenges/4

from challenge3 import decrypt_string_xored_by_single_char, score_string

def decrypt_file(filename):
    lines = []
    with open(filename, "r") as f:
        for line in f:
            lines.append(bytes.fromhex(line.strip()))

    candidates = [decrypt_string_xored_by_single_char(line) for line in lines]

    return max(candidates, key=lambda c: score_string(c["plaintext"]))["plaintext"]


if __name__ == "__main__":
    assert decrypt_file("4.txt") == b"Now that the party is jumping\n"
