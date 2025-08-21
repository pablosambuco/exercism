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

tol = {
    "grey": 0.05,
    "violet": 0.1,
    "blue": 0.25,
    "green": 0.5,
    "brown": 1,
    "red": 2,
    "gold": 5,
    "silver": 10,
}


L = 4


def color_code(color):
    return col.get(color)


def tolerance(color):
    return tol.get(color)


def value(colors):
    l = len(colors)
    return sum(
        10**i * color_code(color)
        for i, color in enumerate(colors[l - 1 :: -1])
    )


def label(colors):
    l = len(colors)

    x = value(colors[: l - 1])
    p = (10 ** color_code(colors[l - 1])) if l > 1 else 1
    x = x * p

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
    x = str(x)
    if x.endswith(".0"):
        x = x[:-2]
    return f"{x} {lab}ohms"


def resistor_label(colors):
    l = len(colors)
    if l not in (1, 4, 5):
        raise ValueError("List of colors must have 1, 4 or 5 elements")
    base = label(colors[:-1]) if l > 1 else label(colors)
    tole = f" ±{tolerance(colors[-1])}%" if l > 1 else ""
    return f"{base}{tole}"
