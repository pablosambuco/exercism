"""twelve days"""

ordinals = [
    "first",
    "second",
    "third",
    "fourth",
    "fifth",
    "sixth",
    "seventh",
    "eighth",
    "ninth",
    "tenth",
    "eleventh",
    "twelfth",
]
presents = [
    "a Partridge in a Pear Tree.",
    "two Turtle Doves,",
    "three French Hens,",
    "four Calling Birds,",
    "five Gold Rings,",
    "six Geese-a-Laying,",
    "seven Swans-a-Swimming,",
    "eight Maids-a-Milking,",
    "nine Ladies Dancing,",
    "ten Lords-a-Leaping,",
    "eleven Pipers Piping,",
    "twelve Drummers Drumming,",
]

base_verse = "On the {} day of Christmas my true love gave to me: {}"


def recite(start_verse, end_verse):
    poem = []
    for verse in range(start_verse - 1, end_verse):
        ordinal = ordinals[verse]
        present_list = (
            " ".join(presents[verse:0:-1])
            + (" and " if verse > 0 else "")
            + presents[0]
        )
        poem.append(base_verse.format(ordinal, present_list))
    return poem
