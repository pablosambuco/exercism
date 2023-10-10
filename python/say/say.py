"""say"""

scale = {
    1000000000: "billion",
    1000000: "million",
    1000: "thousand",
    100: "hundred",
    1: ""
}
quantities = {
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

def say(number):
    if not 0 <= number <= 999999999999:
        raise ValueError("input out of range")
    if number == 0:
        return "zero"
    ss = []
    for s, st in scale.items():
        if number >= s:
            sn = number // s
            sq = []
            for q, qt in quantities.items():
                if sn >= q:
                    sn %= q
                    sq.append(qt)
            number %= s
            ss.append("-".join(sq))
            if st:
                ss.append(st)
    return " ".join(ss)
