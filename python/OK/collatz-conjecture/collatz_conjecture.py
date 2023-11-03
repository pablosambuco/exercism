def steps(number):
    if not isinstance(number, int):
        raise TypeError("Only positive integers are allowed")
    if number <= 0:
        raise ValueError("Only positive integers are allowed")
    n = number
    q = 0
    while n > 1:
        q += 1
        n = n / 2 if n % 2 == 0 else 3 * n + 1
    return q
