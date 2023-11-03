def is_pangram(sentence):
    abc = {chr(x): 0 for x in range(ord("a"), ord("z") + 1)}
    for c in sentence:
        if c.lower() in abc:
            abc[c.lower()] += 1
    return all(abc.values())
