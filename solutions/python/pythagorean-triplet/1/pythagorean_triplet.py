def triplets_with_sum(number):
    if number < 4:
        return None
    squares = [i**2 for i in range(number)]
    pythagoreans = []
    for a in range(1, number // 3 + 1):
        for b in range(a + 1, (number - a) // 2 + 1):
            c = number - a - b
            if squares[a] + squares[b] == squares[c]:
                pythagoreans.append([a, b, c])

    return pythagoreans
