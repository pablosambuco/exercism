def transpose(lines):
    splitted = lines.splitlines()
    out = []
    for j, line in enumerate(splitted):
        localmax = max(len(following) for following in splitted[j:])
        if j == 0:
            out.extend("" for _ in range(localmax))
        for i in range(localmax):
            out[i] += line[i] if i < len(line) else " "
    return "\n".join(out)
