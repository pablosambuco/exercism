""" grep """


def match(line, pattern, i, x):
    eval_line = line.lower() if i else line
    eval_pattern = pattern.lower() if i else pattern
    return eval_line == eval_pattern if x else eval_pattern in eval_line


def read_flags(flags):
    n = False  # Prepend the line number and a colon (':') to each line in the output, placing the number after the filename (if present).
    l = False  # Output only the names of the files that contain at least one matching line.
    i = False  # Match using a case-insensitive comparison.
    v = False  # Invert the program -- collect all lines that fail to match.
    x = False  # Search only for lines where the search string matches the entire line.
    for char in flags:
        if char == "n":
            n = True
        elif char == "l":
            l = True
        elif char == "i":
            i = True
        elif char == "v":
            v = True
        elif char == "x":
            x = True
    return n, l, i, v, x


def grep(pattern, flags, files):
    n, l, i, v, x = read_flags(flags)
    nfiles = len(files)
    response = []
    for file in files:
        with open(file, "r", encoding="utf-8") as f:
            text = f.read().splitlines()
            for j, line in enumerate(text):
                is_match = match(line, pattern, i, x)
                if is_match ^ v:  # XOR: one or another, but not both ;)
                    if l:
                        response.append(file + "\n")
                        break
                    else:
                        rline = (
                            ((file + ":") if nfiles > 1 else "")
                            + ((str(j + 1) + ":") if n else "")
                            + line
                        )
                        response.append(rline + "\n")
    return "".join(response)
