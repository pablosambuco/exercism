import itertools


def maximum_value(maximum_weight, items):
    viable_items = [item for item in items if item["weight"] <= maximum_weight]

    if not viable_items:
        return 0

    max_value = 0
    for i in range(len(viable_items)):
        for combination in itertools.combinations(viable_items, i + 1):
            current_weight = sum(item["weight"] for item in combination)
            if current_weight > maximum_weight:
                continue
            current_value = sum(item["value"] for item in combination)
            if current_value > max_value:
                max_value = current_value
    return max_value
