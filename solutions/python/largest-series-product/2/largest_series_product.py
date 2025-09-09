def largest_product(series, size):
    series = str(series)
    s = len(series)
    if size > s:
        raise ValueError("span must not exceed string length")
    if size < 0:
        raise ValueError("span must not be negative")
    if not series.isnumeric():
        raise ValueError("digits input must only contain digits")

    max_product = 0
    for i in range(s - size + 1):  # for all possible substring
        product = 1
        for j in range(i, i + size):  # calculate the product of their digits
            product *= int(series[j])
        max_product = max(max_product, product)  # and return the maximum

    return max_product
