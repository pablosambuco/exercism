from __future__ import annotations
from math import exp, cos, sin, sqrt


def cls(anything):
    if anything is None:
        return None
    return anything.__class__.__name__


def ensure_complex(func):
    def params(_, anything):
        if not isinstance(anything, ComplexNumber):
            anything = ComplexNumber(anything)
        return func(_, anything)

    return params


class ComplexNumber:
    def __init__(self, real: float, imaginary: float=0):
        self.real = real
        self.imaginary = imaginary

    def __iter__(self):
        return iter((self.real, self.imaginary))

    def __eq__(self, other):
        a, b = self
        c, d = other        
        return a == c and b == d

    @ensure_complex
    def __add__(self, other):
        a, b = self
        c, d = other
        return ComplexNumber(a + c, b + d)

    @ensure_complex
    def __radd__(self, other):
        return other + self

    @ensure_complex
    def __mul__(self, other):
        a, b = self
        c, d = other
        return ComplexNumber(a * c - b * d, a * d + b * c)

    @ensure_complex
    def __rmul__(self, other):
        return other * self

    @ensure_complex
    def __sub__(self, other):
        a, b = self
        c, d = other
        return ComplexNumber(a - c, b - d)

    @ensure_complex
    def __rsub__(self, other):
        return other - self

    @ensure_complex
    def __truediv__(self, other):
        a, b = self
        c, d = other
        c2, d2 = c**2, d**2

        return ComplexNumber((a * c + b * d) / (c2 + d2), (b * c - a * d) / (c2 + d2))

    @ensure_complex
    def __rtruediv__(self, other):
        return other / self

    def __abs__(self):
        a, b = self
        return sqrt(a**2 + b**2)

    def conjugate(self):
        a, b = self
        return ComplexNumber(a, -b)

    def exp(self):
        a, b = self
        return ComplexNumber(exp(a) * cos(b), exp(a) * sin(b))

    def __repr__(self):
        a, b = self
        return f"({a},{b}i)"
