def sum_of_multiples(limit, multiples):
    numbers = set()
    for multiple in multiples:
        if multiple:
            numbers.update([value for value in range(multiple, limit, multiple)])
    return sum(numbers)
