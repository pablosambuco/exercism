"""isogram"""

def is_isogram(string):
    abc = {}
    for c in string:
        if c.lower() in abc:
            return False
        abc[c.lower()] = 0
    return True
