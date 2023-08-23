import string
from textwrap import wrap

DIRECT="abcdefghijklmnopqrstuvwxyz"
INVERT=DIRECT[::-1]

def pos(char):
    return DIRECT.index(char.lower())

def convert(char):
    return INVERT[pos(char)]

def encode(plain_text):
    clean = "".join(
        letter
        for letter in plain_text
        if not letter.isspace() and letter not in string.punctuation
    )
    encoded = "".join(
        convert(letter) if letter.isalpha() else letter
        for letter in clean
    )
    return " ".join(wrap(encoded, 5))      

def decode(ciphered_text):
    return "".join(
        convert(letter) if letter.isalpha() else letter
        for letter in ciphered_text
        if letter != " "
    )
