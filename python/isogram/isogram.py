"""isogram"""


def is_isogram(string):
    abc = {chr(x): 0 for x in range(ord("a"), ord("z") + 1)}
    for c in string:
        if c.lower() in abc:
            if abc[c.lower()] == 1:
                return False
            abc[c.lower()] = 1
    return True
