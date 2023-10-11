def is_correct(chain, dominoes):
    return len(chain) == len(dominoes) and chain[0][0] == chain[-1][1]


def can_chain(dominoes):
    if not dominoes:
        return dominoes

    rest = list(dominoes)
    rest_size = 0
    chain = []
    while rest_size != len(rest):
        rest_size = len(rest)
        link = None
        for domino in rest:
            remove = domino
            if not chain or chain[-1][1] == domino[0]:
                link = domino
                break
            elif chain[-1][1] == domino[1]:
                link = (domino[1], domino[0])
                break
        if link:
            rest.remove(remove)
            chain.append(link)

    if rest:
        new_chain = can_chain(rest)
        if new_chain:
            number = new_chain[0][0]
            pos = next((chain.index(link) for link in chain if link[1] == number), -1)
            if pos != -1:
                while new_chain:
                    link = new_chain.pop()
                    if link in rest:
                        rest.remove(link)
                    else:
                        rest.remove((link[1], link[0]))
                    chain.insert(pos + 1, link)

    while rest:
        number = rest[-1][0]
        pos = next((chain.index(link) for link in chain if link[1] == number), -1)
        if pos == -1:
            break
        chain.insert(pos + 1, rest.pop())

    return chain if is_correct(chain, dominoes) else None
