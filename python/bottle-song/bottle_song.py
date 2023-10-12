"""Bottle song"""

base_verse = "{} green bottle{} hanging on the wall,"
fall_verse = "And if one green bottle should accidentally fall,"
will_verse = "There'll be {} green bottle{} hanging on the wall."

parts = {
    1: ("One", "", "no", "s"),
    2: ("Two", "s", "one", ""),
    3: ("Three", "s", "two", "s"),
    4: ("Four", "s", "three", "s"),
    5: ("Five", "s", "four", "s"),
    6: ("Six", "s", "five", "s"),
    7: ("Seven", "s", "six", "s"),
    8: ("Eight", "s", "seven", "s"),
    9: ("Nine", "s", "eight", "s"),
    10: ("Ten", "s", "nine", "s"),
}


def recite(start, take=1):
    poem = []
    for _ in range(take):
        number, plural, will, pwill = parts[start]
        poem.extend(
            (
                base_verse.format(number, plural),
                base_verse.format(number, plural),
                fall_verse,
                will_verse.format(will, pwill),
                "",
            )
        )
        start -= 1
    return poem[:-1]
