def spiral_matrix(size):
    matrix = [[0 for _ in range(size)] for _ in range(size)]
    limits = [-1, 0, size - 1, size - 1]
    inc_cols, inc_rows = 1, 0
    end = [False, False]
    i = j = k = 0
    change = False
    while size and not all(end):
        matrix[j][i] = k + 1

        i += inc_cols
        j += inc_rows
        k += 1

        if i > limits[2]:
            i -= 1
            change = True
            limits[0] += 1
            inc_cols, inc_rows = 0, 1

        if j > limits[3]:
            j -= 1
            change = True
            limits[1] += 1
            inc_cols, inc_rows = -1, 0

        if i < limits[0]:
            i += 1
            change = True
            limits[2] -= 1
            inc_cols, inc_rows = 0, -1

        if j < limits[1]:
            j += 1
            change = True
            limits[3] -= 1
            inc_cols, inc_rows = 1, 0

        if limits[0] == limits[2]:
            end[0] = True

        if limits[1] == limits[3]:
            end[1] = True

        if change:
            change = False
            k -= 1

    return matrix
