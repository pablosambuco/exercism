def saddle_points(matrix):
    rows = len(matrix)
    if not rows:
        return []

    cols = len(matrix[0])
    r_rows = range(rows)
    r_cols = range(cols)

    # test regularity
    if any([len(matrix[i]) != cols for i in r_rows]):
        raise ValueError("irregular matrix")

    # get columns minimums and rows maximums
    col_mins = [min([matrix[i][j] for i in r_rows]) for j in r_cols]
    row_maxs = [max([matrix[i][j] for j in r_cols]) for i in r_rows]

    # get the points where the column minimum is equal to the row maximum
    return [
        {"row": i + 1, "column": j + 1}
        for j in r_cols
        for i in r_rows
        if col_mins[j] == row_maxs[i]
    ]
