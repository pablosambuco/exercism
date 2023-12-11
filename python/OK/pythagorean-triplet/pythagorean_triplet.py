def triplets_with_sum(number):
    # Premises:
    #
    # a + b + c = number
    # a < b < c
    # a**2 + b**2 = c**2 => c = (a**2 + b**2) ** (1/2)
    # =>
    # a + b - number = (a**2 + b**2) ** (1/2)
    # (a + b - number)**2 = a**2 + b**2
    # a**2 + a.b - a.number + b**2 + a.b - b.number - a.number - b.number + number**2 = a**2 + b**2
    # a**2 + b**2 + 2.a.b - 2.a.number - 2.b.number + number**2 = a**2 + b**2
    # =>
    # 2.a.b - 2.a.number - 2.b.number + number**2 = 0
    # b(2a - 2number) - number(2a - number) = 0
    # b = number(2a - number)/2(a - number)
    #
    if number < 4:
        return None
    pythagoreans = []
    for a in range(1, number // 3 + 1):
        b = number * (2 * a - number) / (2 * (a - number))
        if a < b and b % 1 == 0:
            b = int(b)
            c = number - a - b
            pythagoreans.append([a, b, c])

    return pythagoreans
