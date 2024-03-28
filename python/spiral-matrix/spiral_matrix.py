from itertools import cycle


def spiral_matrix(size):
    matrix = [[0 for _ in range(size)] for _ in range(size)]
    increment = cycle([(0, 1), (1, 0), (0, -1), (-1, 0)])
    i = j = k = 0
    r, c = next(increment)

    for k in range(size**2):
        if not (0 <= j + c < size and 0 <= i + r < size and matrix[i + r][j + c] == 0):
            r, c = next(increment)
        matrix[i][j] = k + 1
        i, j = i + r, j + c

    return matrix
