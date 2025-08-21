"""
Diffie-Hellman key exchange.

Since this is only an exercise, `random` is fine to use, but note that **it would be
very insecure if actually used for cryptography.**

"""
import random


def private_key(p):
    return random.randint(2, p-1)


def public_key(p, g, private):
    return g**private % p


def secret(p, public, private):
    return public**private % p
