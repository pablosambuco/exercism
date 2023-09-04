def cipher_text(plain_text):
    normalized = "".join([char for char in plain_text if char.isalnum()]).lower()
    length = len(normalized)
    if not length:
        return ""
    rows = cols = int(length ** (0.5))
    if rows * cols < length:
        cols += 1
    if rows * cols < length:
        rows += 1
    padding = rows * cols - length
    normalized += " " * padding
    # transposing columns and rows for everything thar follows
    out = [[[] for _ in range(rows)] for _ in range(cols)]
    for pos, char in enumerate(normalized):
        c, r = divmod(pos, cols)
        out[r][c] = char
    return " ".join("".join(row) for row in out)
