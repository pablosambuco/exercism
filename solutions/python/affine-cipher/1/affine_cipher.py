"""Affine Cipher"""

import string
from textwrap import wrap

M = 26  # Latin alphabet size


def coprime_with_m(a):
    return not any(1 < i <= a and a % i == 0 and M % i == 0 for i in range(a + 1))


def index(letter):
    return ord(letter.lower()) - ord("a")


def char(idx):
    return chr(ord("a") + idx)


def mmi(A):
    return next((i for i in range(M) if i > 0 and (A * i) % M == 1), 1)


def coprime_check(func):
    def wrapper(*args, **kwargs):
        a = args[1]
        if not coprime_with_m(a):
            raise ValueError("a and m must be coprime.")
        return func(*args, **kwargs)

    return wrapper


@coprime_check
def encode(plain_text, a, b):
    """E(x) = (ai + b) mod m"""
    clean = "".join(
        letter
        for letter in plain_text
        if not letter.isspace() and letter not in string.punctuation
    )
    encoded = "".join(
        char((a * index(letter) + b) % M) if letter.isalpha() else letter
        for letter in clean
    )
    return " ".join(wrap(encoded, 5))


@coprime_check
def decode(ciphered_text, a, b):
    """D(y) = (a^-1)(y - b) mod m"""
    return "".join(
        char((mmi(a) * (index(letter) - b)) % M) if letter.isalpha() else letter
        for letter in ciphered_text
        if letter != " "
    )
