"""prime factors"""


def factors(number):
    f = []
    if number <= 1:
        return []
    n = 2
    while number > 1:
        while number % n == 0:
            f.append(n)
            number //= n
        n += 1

    return f
