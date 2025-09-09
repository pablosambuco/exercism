

def annotate(garden):

    if not garden:
        return []

    if any(any(c not in ["*", " "] for c in l) or len(l) != len(garden[0]) for l in garden):
        raise ValueError("The board is invalid with current input.")

    adjacents = [(x, y) for y in (-1, 0, 1) for x in (-1, 0, 1) if x or y]
    rows = len(garden)
    cols = len(garden[0])

    for i in range(rows):
        for j in range(cols):
            row = list(garden[i])
            if garden[i][j] == " ":
                q = 0
                for x, y in adjacents:
                    if (
                            i + x >= 0 and i + x < rows
                        and j + y >= 0 and j + y < cols
                        and garden[i + x][j + y] == "*"
                    ):
                        q += 1
                if q:
                    row[j] = str(q)
            garden[i] = "".join(row)
    return garden
