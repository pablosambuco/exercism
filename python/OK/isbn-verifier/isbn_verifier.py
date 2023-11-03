def is_valid(isbn):
    clean = isbn.replace("-", "")
    if (
        len(clean) != 10
        or not clean[:-1].isnumeric()
        or not clean[-1].isnumeric()
        and clean[-1] != "X"
    ):
        return False
    verif = 0
    for p, v in enumerate(isbn.replace("-", "")[::-1]):
        if v == "X":
            v = 10
        verif += (p + 1) * int(v)
        print((p + 1), int(v), (p + 1) * int(v), verif, verif % 11)

    return not verif % 11
