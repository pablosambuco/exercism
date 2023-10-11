"""say"""

thousands = {
    1000000000: "billion",
    1000000: "million",
    1000: "thousand",
    100: "hundred",
    1: "",
}

numbers = {
    100: "hundred",
    90: "ninety",
    80: "eighty",
    70: "seventy",
    60: "sixty",
    50: "fifty",
    40: "forty",
    30: "thirty",
    20: "twenty",
    19: "nineteen",
    18: "eighteen",
    17: "seventeen",
    16: "sixteen",
    15: "fifteen",
    14: "fourteen",
    13: "thirteen",
    12: "twelve",
    11: "eleven",
    10: "ten",
    9: "nine",
    8: "eight",
    7: "seven",
    6: "six",
    5: "five",
    4: "four",
    3: "three",
    2: "two",
    1: "one",
}


def factorice(number, factors):
    number_dict = {}
    for factor in factors:
        value, number = divmod(number, factor)
        if value:
            number_dict[factor] = value
    return number_dict


def say(number):
    if not 0 <= number <= 999999999999:
        raise ValueError("input out of range")

    if number == 0:
        return "zero"

    big_scale = factorice(number, thousands)
    for number in big_scale:
        big_scale[number] = factorice(big_scale[number], numbers)

    number_list = []
    sep = " "
    while big_scale:
        scale, value = big_scale.popitem()
        number_list.insert(0, sep)
        number_list.insert(0, thousands[scale])
        previous = 999
        while value:
            small_scale, small_value = value.popitem()
            separator = " "
            if previous < 100 and small_scale < 100:
                separator = "-"
            number_list.insert(0, separator)
            number_list.insert(0, numbers[small_scale])
            if small_value > 1:
                number_list.insert(0, separator)
                number_list.insert(0, numbers[small_value])
            previous = small_scale

    return "".join(number_list).strip()
