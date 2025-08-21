def flatten(iterable: list):
    flat = []
    for item in iterable:
        data = flatten(item) if hasattr(item, "__iter__") else [item]
        flat.extend(x for x in data if x is not None)
    return flat
