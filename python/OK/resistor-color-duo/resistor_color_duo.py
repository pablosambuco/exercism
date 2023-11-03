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

L = 2


def color_code(color):
    return col.get(color)


def value(colors):
    l = len(colors)
    if l < L:
        raise ValueError("List of colors must have at least 2 elements")
    return sum(
        10**i * color_code(color)
        for i, color in enumerate(colors[L - 1 :: -1])
        if i < L
    )
