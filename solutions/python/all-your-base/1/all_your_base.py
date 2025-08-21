def rebase(input_base, digits, output_base):
    if input_base < 2:
        raise ValueError("input base must be >= 2")

    if output_base < 2:
        raise ValueError("output base must be >= 2")

    for c in digits:
        if c < 0 or c >= input_base:
            raise ValueError("all digits must satisfy 0 <= d < input base")

    value = sum(input_base**p * v for p, v in enumerate(digits[::-1]))
    ret = []
    while value:
        digit = value % output_base
        ret.append(digit)
        value = (value - digit) / output_base
    if not ret:
        ret = [0]

    return ret[::-1]
