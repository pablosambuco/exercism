col = {
    "black": 0,
    "brown": 1,
    "red": 2,
    "orange": 3,
    "yellow": 4,
    "green": 5,
    "blue": 6,
    "violet": 7,
    "grey": 8,
    "white": 9,
}


L = 3


def color_code(color):
    return col.get(color)


def value(colors):
    l = len(colors)
    return sum(
        10**i * color_code(color)
        for i, color in enumerate(colors[l - 1 :: -1])
    )


def label(colors):
    l = len(colors)
    if l < L:
        raise ValueError("List of colors must have at least 3 elements")

    x = value(colors[:L-1]) * (10 ** color_code(colors[L-1]))

    if x > 10**9:
        lab = "giga"
        x = x / 10**9
    elif x > 10**6:
        lab = "mega"
        x = x / 10**6
    elif x > 10**3:
        lab = "kilo"
        x = x / 10**3
    else:
        lab = ""
    return f"{x} {lab}ohms"
