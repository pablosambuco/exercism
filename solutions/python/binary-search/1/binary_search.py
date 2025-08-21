def find_rec(search_list, value, start, end):
    middle = (start + end) // 2
    if search_list[middle] == value:
        return middle
    if start == end:
        raise ValueError("value not in array")
    if search_list[middle] > value:
        return find_rec(search_list, value, start, middle)
    if search_list[middle] < value:
        return find_rec(search_list, value, middle + 1, end)


def find(search_list, value):
    largo = len(search_list)
    if largo:
        return find_rec(search_list, value, 0, largo - 1)
    raise ValueError("value not in array")
