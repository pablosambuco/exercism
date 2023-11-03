def fence(rails):
    return [[] for _ in range(rails)]


def positions(rails):
    return list(range(rails)) + list(range(rails - 2, 0, -1))


def assignments(pos, msg):
    return list(pos * ((len(msg) + len(pos) - 1) // len(pos)))[: len(msg)]


def encode(message, rails):
    f = fence(rails)
    assign = assignments(positions(rails), message)

    for i in range(len(message)):
        f[assign[i]].append(message[i])

    return "".join("".join(x) for x in f)


def decode(message, rails):
    f = fence(rails)
    assign = assignments(positions(rails), message)

    text = list(message[::-1])
    lengths = {x: assign.count(x) for x in assign}
    for i in range(rails):
        for _ in range(lengths[i]):
            f[i].insert(0, text.pop())

    decoded_chars = [f[assign[i]].pop() for i in range(len(message))]
    return "".join(decoded_chars)
