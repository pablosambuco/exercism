"""triangles
"""


def bad_triangle(a, b, c):
    return a == 0 or b == 0 or c == 0 or a + b < c or a + c < b or b + c < a


def equilateral(sides):
    a = sides[0]
    b = sides[1]
    c = sides[2]
    return not bad_triangle(a, b, c) and a == b == c


def isosceles(sides):
    a = sides[0]
    b = sides[1]
    c = sides[2]
    return not bad_triangle(a, b, c) and (a == b or a == c or b == c)


def scalene(sides):
    a = sides[0]
    b = sides[1]
    c = sides[2]
    return not bad_triangle(a, b, c) and a != b and a != c and b != c
