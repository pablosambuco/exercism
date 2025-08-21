from __future__ import annotations
from math import gcd


class Rational:
    def __init__(self, numer, denom):
        if denom < 0:
            numer *= -1
            denom *= -1

        x = gcd(numer, denom)
        self.numer = numer // x
        self.denom = denom // x

    def inverse(self):
        self.numer, self.denom = self.denom, self.numer

    def __eq__(self, other: Rational):
        return self.numer == other.numer and self.denom == other.denom

    def __repr__(self):
        return f"{self.numer}/{self.denom}"

    def __add__(self, other: Rational):
        return Rational(
            self.numer * other.denom + other.numer * self.denom,
            self.denom * other.denom,
        )

    def __sub__(self, other: Rational):
        return Rational(
            self.numer * other.denom - other.numer * self.denom,
            self.denom * other.denom,
        )

    def __mul__(self, other: Rational):
        return Rational(self.numer * other.numer, self.denom * other.denom)

    def __truediv__(self, other: Rational):
        return self * other.inverse()

    def __abs__(self):
        return Rational(abs(self.numer), self.denom)

    def __pow__(self, power):
        if power < 0:
            power *= -1
            return self.inverse() ** power
        return Rational(self.numer**power, self.denom**power)

    def __rpow__(self, base):
        return base ** (self.numer / self.denom)
