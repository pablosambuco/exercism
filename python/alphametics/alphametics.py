def solve(puzzle):
    puzzle = "SEND + MORE == MONEY"
    words = puzzle.split()
    words.remove("+")
    words.remove("==")

    counts = {}
    translation = {}
    for word in words:
        for letter in word:
            if letter.isalpha():
                counts[letter] = counts.get(letter, 0) + 1

    if words:
        if len(words[-1]) > len(words[0]):
            translation[words[-1][0]] = "1"

    #TODO TERMINAR ESTO!