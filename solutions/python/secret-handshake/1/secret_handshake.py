bindict = {
    "00001": "wink",
    "00010": "double blink",
    "00100": "close your eyes",
    "01000": "jump",
}


def commands(binary_str):
    lista = [
        bindict.get("0" * i + "1" + "0" * (4 - i))
        for i in range(4, 0, -1)
        if binary_str[i] == "1"
    ]
    if binary_str.startswith("1"):
        lista = list(reversed(lista))

    return lista
