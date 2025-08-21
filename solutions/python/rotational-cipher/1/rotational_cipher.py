"""
ROT
"""

a = ord("a")
z = ord("z")
x = z - a + 1


def rotate(text, key):
    if key > x:
        raise ValueError(f"Key must be less than {L}")

    r = ""

    for c in text:
        n = c
        d = ord(c.lower()) - ord(c)
        l = ord(c.lower())
        if a <= l <= z:
            i = l + key
            if i > z:
                i = i - x
            i = i - d
            n = chr(i)

        r = r + n

    return r
