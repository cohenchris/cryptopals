#!/bin/python

# https://cryptopals.com/sets/2/challenges/9

def pkcs7_pad(data, block_size):
    if len(data) % block_size == 0:
        return data

    padding_size = block_size - (len(data) % block_size)
    padding = chr(padding_size).encode()

    return data + padding * padding_size


def pkcs7_unpad(data, block_size):
    for size in range(block_size):
        pad = chr(size).encode()
        if data[-size:] == (pad * size):
            return data[:-size]
    return data


if __name__ == "__main__":
    data = b'YELLOW SUBMARINE'
    block_size = 20
    padded = pkcs7_pad(data, block_size)

    assert padded == b'YELLOW SUBMARINE\x04\x04\x04\x04'
