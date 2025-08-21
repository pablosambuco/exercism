"""
This exercise stub and the test suite contain several enumerated constants.

Since Python 2 does not have the enum module, the idiomatic way to write
enumerated constants has traditionally been a NAME assigned to an arbitrary,
but unique value. An integer is traditionally used because it’s memory
efficient.
It is a common practice to export both constants and functions that work with
those constants (ex. the constants in the os, subprocess and re modules).

You can learn more here: https://en.wikipedia.org/wiki/Enumerated_type
"""

# Possible sublist categories.
# Change the values as you see fit.
SUBLIST = -1
SUPERLIST = 1
EQUAL = 2
UNEQUAL = 0


def sublist(a, b):
    if not a and not b:
        return EQUAL
    if a == b:
        return EQUAL
    if not b:
        return SUPERLIST
    if not a:
        return SUBLIST
    x = len(a)
    y = len(b)
    if x > y:
        return sublist(b, a) * -1
    for a_ in a:
        if a_ in b:
            for j in range(y):
                if y - j < x:
                    return UNEQUAL
                if a == b[j : j + x]:
                    return SUBLIST
    return UNEQUAL
