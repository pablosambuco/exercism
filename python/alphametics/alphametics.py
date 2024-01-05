from string import digits
from copy import deepcopy

FILLER = " "  # any non-alphabetic character
REPLACEMENTS = str.maketrans("+=", "  ")


def solve(puzzle: str) -> dict:
    words = puzzle.translate(REPLACEMENTS).split()
    letters = set(list("".join(words)))
    if not 0 < len(letters) <= 10:
        return {}

    operands = len(words) - 1
    # if only result:
    if operands == 0:
        return None
    # if only one operand and its not exactly equal to the result:
    if len(words[:-1]) == 1 and words[0] != words[-1]:
        return None

    # calculate lengths for every word
    lengths = [len(word) for word in words]
    max_length = max(lengths)

    # fill possible translations for every letter in the puzzle
    tran = {letter: list(digits) for letter in letters}

    # justify all words to the right
    words = [word.rjust(max_length, FILLER) for word in words]

    # generate every formula possible
    sums = [list(operation) for operation in (zip(*words))][::-1]
    for i in range(len(sums)):
        while FILLER in sums[i]:
            sums[i].remove(FILLER)

    # removing 0 from the translation for the leftmost character of every word:
    for word in words:
        for letter in word:
            if letter != FILLER:
                remove_translation(tran, letter, "0")
                break

    # if the length of the result is greater than the length of all operands
    # check the maximum value for the carry
    if all(max_length > length for length in lengths[:-1]):
        max_values = [str(x + 1) for x in range(int(str(operands - 1)[0]))]
        set_translation(tran, words[-1][0], max_values)

    tran = brute_force(tran, sums)
    if not tran:
        return None
    solution = {x: int(y[0]) for x, y in tran.items() if x != FILLER}
    solution_values = list(solution.values())
    if any(solution_values.count(value) > 1 for value in solution_values):
        return None
    return solution


def test(tran: dict, sums: list, level=0) -> bool:
    if any(len(v) > 1 for _, v in tran.items()):
        return False
    carry = 0
    for s in sums:
        *operands, result = s
        for i in range(len(operands)):
            operands[i] = int(tran[operands[i]][0])
        result = int(tran[result][0])
        real_result = sum(operands) + carry
        carry, real_result = divmod(real_result, 10)
        if result != real_result:
            return False
    return True


def set_translation(tran: dict, orig: str, dest: list) -> None:
    for value in tran:
        if value == orig:
            tran[value] = dest
        else:
            if len(dest) == 1 and dest[0] in tran[value]:
                tran[value].remove(dest[0])


def remove_translation(tran: dict, orig: str, dest: str) -> None:
    if dest in tran[orig]:
        tran[orig].remove(dest)


def brute_force(tran: dict, sums: list, level=0) -> dict:
    # try every transalation possible recursively, it's slooooooooooooooooooooow
    new_tran = {}
    if all(len(tran[letter]) == 1 for letter in tran):
        if test(tran, sums, level):
            return tran
    for letter in tran:
        if len(tran[letter]) > 1:
            for value in tran[letter]:
                new_tran = deepcopy(tran)
                set_translation(new_tran, letter, [value])
                deep_tran = brute_force(new_tran, sums, level + 1)
                if deep_tran:
                    return deep_tran
