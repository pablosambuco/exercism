"""
minesweeper annotate
"""


def validate(minefield, l_size, c_size):
    """
    Validates the minefield boarsd.

    Args:
        minefield: A list of strings representing the minefield board.
        l_size: The number of lines.
        c_size: The number of columns.

    Raises:
        ValueError: If the board is invalid
    """
    if any(
        len(line) != c_size or any(char not in ("*", " ") for char in line)
        for line in minefield
    ):
        raise ValueError("The board is invalid with current input.")


def annotate(minefield):
    """
    Annotates a board with the number of mines in adjacent squares

    Args:
        minefield: A list of strings representing the minefield board.

    Returns:
        list: annotated minefield
    """
    if not minefield:
        return []

    l_size, c_size = len(minefield), len(minefield[0])

    validate(minefield, l_size, c_size)

    lines = [[0 if char == " " else char for char in line] for line in minefield]

    for i in range(l_size):
        for j in range(c_size):
            if lines[i][j] == "*":
                continue
            l_lo, l_hi = max(0, i - 1), min(l_size, i + 2)
            c_lo, c_hi = max(0, j - 1), min(c_size, j + 2)
            for l in range(l_lo, l_hi):
                for c in range(c_lo, c_hi):
                    if lines[l][c] == "*":
                        lines[i][j] += 1

    return ["".join(" " if char == 0 else str(char) for char in line) for line in lines]
