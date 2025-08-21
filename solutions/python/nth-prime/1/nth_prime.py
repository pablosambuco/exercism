"""
Nth prime
"""

primeslist = [2]


def is_prime(number):
    return all(number % n != 0 for n in primeslist)


def prime(number):
    if number < 1:
        raise ValueError("there is no zeroth prime")
    n = len(primeslist)
    i = 3
    while n < number:
        if is_prime(i):
            primeslist.append(i)
        n = len(primeslist)
        i += 1
    return primeslist[number - 1]
