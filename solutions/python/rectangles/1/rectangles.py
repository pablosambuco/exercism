def rectangles(strings):
    lines = len(strings)
    if not lines:
        return 0
    columns = len(strings[0])
    if not columns:
        return 0
    q = 0
    for i in range(lines):
        for j in range(i + 1, lines):
            for k in range(columns):
                for l in range(k + 1, columns):
                    if (
                        strings[i][k] == "+"
                        and strings[i][l] == "+"
                        and strings[j][k] == "+"
                        and strings[j][l] == "+"
                    ):
                        rectangle = True
                        for x in range(i, j + 1):
                            for y in range(k, l + 1):
                                if (
                                    x in (i, j)
                                    and strings[x][y] not in "+-"
                                    or y in (k, l)
                                    and strings[x][y] not in "+|"
                                ):
                                    rectangle = False
                        if rectangle:
                            q += 1
    return q
