from __future__ import annotations
from math import exp, cos, sin, sqrt


def cls(anything):
    if anything is None:
        return None
    return anything.__class__.__name__


class ComplexNumber:
    def __init__(self, real: float, imaginary: float):
        self.real = real
        self.imaginary = imaginary

    def __eq__(self, other):
        return self.real == other.real and self.imaginary == other.imaginary

    def __add__(self, other):
        if cls(other) == "ComplexNumber":
            # (a + bi) + (c + di) = (a+c + bi+di)
            return ComplexNumber(
                self.real + other.real,
                self.imaginary + other.imaginary,
            )
        if cls(other) in ("int", "float"):
            return ComplexNumber(
                self.real + other,
                self.imaginary,
            )

    def __radd__(self, other):
        return self.__add__(other)

    def __mul__(self, other):
        if cls(other) == "ComplexNumber":
            # (a + bi).(c + di) = a.c +a.di + bi.c + bi.di = (ac-bd,adi+bci)
            return ComplexNumber(
                self.real * other.real - self.imaginary * other.imaginary,
                self.real * other.imaginary + self.imaginary * other.real,
            )
        if cls(other) in ("int", "float"):
            return ComplexNumber(
                self.real * other,
                self.imaginary * other,
            )

    def __rmul__(self, other):
        return self.__mul__(other)

    def __sub__(self, other):
        if cls(other) == "ComplexNumber":
            # (a + bi) - (c + di) = (a-c + bi-di)
            return ComplexNumber(
                self.real - other.real,
                self.imaginary - other.imaginary,
            )
        if cls(other) in ("int", "float"):
            return ComplexNumber(
                self.real - other,
                self.imaginary,
            )

    def __rsub__(self, other):
        return ComplexNumber(
            other - self.real,
            -self.imaginary,
        )

    def __truediv__(self, other):
        if cls(other) == "ComplexNumber":
            # (a + bi) / (c + di) = (a.c + b.d)/(c.c + d.d) + (b.c i - a.d i)/(c.c + d.d)`.
            return ComplexNumber(
                (self.real * other.real + self.imaginary * other.imaginary) / (other.real**2 + other.imaginary**2),
                (self.imaginary * other.real - self.real * other.imaginary) / (other.real**2 + other.imaginary**2),
            )
        if cls(other) in ("int", "float"):
            return ComplexNumber(
                self.real / other,
                self.imaginary / other,
            )

    def __rtruediv__(self, other):
        return ComplexNumber(other, 0) / self

    def __abs__(self):
        return sqrt(self.real**2 + self.imaginary**2)

    def conjugate(self):
        return ComplexNumber(
            self.real,
            -self.imaginary,
        )

    def exp(self):
        # e^(a + bi) = e^a.cos(b) + e^a.sin(b)i`
        return ComplexNumber(
            exp(self.real) * cos(self.imaginary),
            exp(self.real) * sin(self.imaginary),
        )

    def __repr__(self):
        return f"({self.real},{self.imaginary}i)"
