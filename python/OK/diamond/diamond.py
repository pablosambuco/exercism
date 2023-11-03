"""Diamond"""


def rows(letter: str):
    position = ord(letter) - ord("A")

    lines = []
    for i in range(position + 1):
        line = "".join(
            [
                chr(i + ord("A")) if abs(position - j) - i == 0 else " "
                for j in range((position + 1) * 2 - 1)
            ]
        )
        lines.append(line)

    return lines + lines[:-1][::-1]
