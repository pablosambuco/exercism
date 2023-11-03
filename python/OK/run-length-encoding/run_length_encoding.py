"""RLE"""


def decode(string):
    out = []
    number = 0
    for char in string:
        if char.isnumeric():
            number = number * 10 + int(char)
        else:
            out.extend([char] * (number or 1))
            number = 0
    return "".join(out)


def encode(string):
    if not string:
        return ""
    out = []
    count = 1
    for i in range(1, len(string)):
        if string[i] == string[i - 1]:
            count += 1
        else:
            out.extend((str(count) if count > 1 else "", string[i - 1]))
            count = 1
    out.extend((str(count) if count > 1 else "", string[-1]))
    return "".join(out)
