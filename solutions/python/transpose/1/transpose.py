def transpose(lines):
    splitted = lines.splitlines()

    maxlen = []
    for i in range(len(splitted)):
        localmax = 0
        for j, line in enumerate(splitted):
            current = len(line)
            if i <= j and localmax <= current:
                localmax = current
        maxlen.append(localmax)

    out = []
    for j, line in enumerate(splitted):
        for i in range(maxlen[j]):
            if j == 0:
                out.append(line[i] if i < len(line) else " ")
            else:
                out[i] += line[i] if i < len(line) else " "
    return "\n".join(out)
