"""wordy"""

known_words = ["plus", "minus", "multiplied", "divided", "by"]
ops = {"plus": "+", "minus": "-", "multiplied": "*", "divided": "/"}


def is_numeric(value):
    try:
        float(value)
        return True
    except ValueError:
        return False


def parse(question):
    words = question[:-1].split()  # removes question mark
    operands = []
    if not words or words[0] != "What":  # empty or not a "what is" question
        raise ValueError("unknown operation")

    clean = []
    for word in words[2:]:  # check valid operations and numbers
        if not (word in known_words or is_numeric(word)):
            raise ValueError("unknown operation")
        if word != "by":
            clean.append(word)

    nex = "n"  # first word must be numeric
    for word in clean:
        if nex == "o" and word in ops:  # next must operation, and it is
            operands.append(ops[word])
            nex = "n"  # next must be numeric
        elif nex == "n":  # word is not operation and we expect a number
            operands.append(word)
            nex = "o"  # next must be operation
        else:
            raise ValueError("syntax error")

    if nex == "n":  # incomplete question
        raise ValueError("syntax error")

    return operands[::-1]


def answer(question):
    items = parse(question)
    ans = items.pop()
    while items:
        ans = f"({ans}) {items.pop()} {items.pop()}"

    return eval(ans)
