"""killer sudoku helper"""
import itertools


def combinations(target, size, exclude):
    numbers = [num for num in range(1, 10) if num <= target and num not in exclude]
    if not numbers:
        return []

    return [
        list(comb)
        for comb in itertools.combinations(numbers, size)
        if sum(comb) == target
    ]
