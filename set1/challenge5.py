#!/bin/python

# https://cryptopals.com/sets/1/challenges/5

def repeating_key_xor(string, key):
    result = b''
    for i in range(len(string)):
        s = string[i]
        k = key[i % len(key)]
        xor = s ^ k
        result += xor.to_bytes(1, 'big')

    return result.hex().encode()




string = b"Burning 'em, if you ain't quick and nimble\nI go crazy when I hear a cymbal"
key = b'ICE'

if __name__ == "__main__":
    assert repeating_key_xor(string, key) == b'0b3637272a2b2e63622c2e69692a23693a2a3c6324202d623d63343c2a26226324272765272a282b2f20430a652e2c652a3124333a653e2b2027630c692b20283165286326302e27282f'
