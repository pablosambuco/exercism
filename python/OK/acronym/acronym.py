def valid(char):
    return char.isalpha() or char == "'"


def abbreviate(words):
    acronym = ""
    prev_is_not_valid = True
    for char in words:
        char_is_valid = valid(char)
        if char_is_valid and prev_is_not_valid:
            acronym += char
        prev_is_not_valid = not char_is_valid
    return acronym.upper()
