#!/bin/python

from pprint import pprint
from Crypto.Cipher import AES

from challenge7 import aes_128_ecb_decrypt
from challenge10 import aes_128_ecb_encrypt
from challenge11 import aes_keygen

class Oracle:
    def __init__(self):
        self._key = aes_keygen()

    def encrypt_profile(self, profile):
        """
        Generate random AES key and encrypt the profile
        under the key, then return ciphertext to client.
        """

        # Transform profile into bytes
        profile = profile.encode('utf-8')
        ciphertext = aes_128_ecb_encrypt(profile, self._key)
        return ciphertext

    def decrypt_profile(self, ciphertext):
        """
        Decrypt the ciphertext and parse the data as a
        user profile.
        """
        plaintext = aes_128_ecb_decrypt(ciphertext, self._key).decode('utf-8')
        json_plaintext = split_cookie(plaintext)
        return json_plaintext


def split_cookie(cookie_str):
    """
    Takes the format:
        foo=bar&baz=qux&zap=zazzle
    And turns it into:
        {
            foo: 'bar',
            baz: 'qux',
            zap: 'zazzle'
        }
    """
    fields = cookie_str.split("&")
    split = {}
    for field in fields:
        s = field.split("=")
        split[s[0]] = s[1]

    return split


def profile_for(email):
    """
    Creates a 'profile' for the user
    with the passed in email, encoded
    in the following format:
        foo=bar&baz=qux&zap=zazzle
    """

    # Strip metacharacters from the passed in email
    metachars = "&="
    [email := email.replace(metachar, "") for metachar in metachars]

    uid = "10"
    role = "user"
    profile = f"email={email}&uid={uid}&role={role}"

    return profile


def ecb_cut_and_paste(oracle):
    """
    Taking in an encrypted profile, escalate the role from
    'user' to 'admin'
    """

    padding_len = AES.block_size - len("admin")
    padding = chr(padding_len) * padding_len
    admin_encrypted = oracle.encrypt_profile("admin" + padding)
    admin_payload = admin_encrypted[:16]

    email = "chris@chr.dev"
    normal_profile = profile_for(email)
    normal_encrypted = oracle.encrypt_profile(normal_profile)
    normal_payload = normal_encrypted[:32]

    escalated_payload = normal_payload + admin_payload

    return escalated_payload


if __name__ == "__main__":
    json_cookie = {"foo": "bar", "baz": "qux", "zap": "zazzle"}
    cookie = "foo=bar&baz=qux&zap=zazzle"
    split = split_cookie(cookie)
    assert split == json_cookie

    oracle = Oracle()

    admin_profile = {"email": "chris@chr.dev", "uid": "10", "role": "admin"}
    escalated_profile = ecb_cut_and_paste(oracle)
    assert oracle.decrypt_profile(escalated_profile) == admin_profile

