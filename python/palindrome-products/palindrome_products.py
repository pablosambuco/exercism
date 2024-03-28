"""
palindromic product
"""


def is_palindrome(number):
    original_number = number
    reversed_number = 0
    while number:
        reversed_number = reversed_number * 10 + number % 10
        number //= 10
    return original_number == reversed_number


def largest(min_factor, max_factor):
    """Given a range of numbers, find the largest palindromes which
       are products of two numbers within that range.

    :param min_factor: int with a default value of 0
    :param max_factor: int
    :return: tuple of (palindrome, iterable).
             Iterable should contain both factors of the palindrome in an arbitrary order.
    """
    if min_factor > max_factor:
        raise ValueError("min must be <= max")

    for product in range(max_factor * max_factor + 1, min_factor * min_factor, -1):
        if is_palindrome(product):
            factors = []
            for i in range(min_factor, max_factor +1):
                if product % i == 0 and min_factor <= product//i <= max_factor:
                    factors.append([product//i, i])
            if factors:
                return (product, factors)
    return (None, [])


def smallest(min_factor, max_factor):
    """Given a range of numbers, find the smallest palindromes which
    are products of two numbers within that range.

    :param min_factor: int with a default value of 0
    :param max_factor: int
    :return: tuple of (palindrome, iterable).
    Iterable should contain both factors of the palindrome in an arbitrary order.
    """
    if min_factor > max_factor:
        raise ValueError("min must be <= max")

    for product in range(min_factor * min_factor, max_factor * max_factor + 1):
        if is_palindrome(product):
            factors = []
            for i in range(min_factor, max_factor +1):
                if product % i == 0 and min_factor <= product//i <= max_factor:
                    factors.append([product//i, i])
            if factors:
                return (product, factors)
    return (None, [])
