"""Newtons approximation to square root"""


def square_root(n):
    px = n  # Initial guess
    while True:
        x = 0.5 * (px + n / px)
        if abs(px - x) < 1:
            return int(x)  # best approximation
        px = x