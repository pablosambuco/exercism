"""food chain poem"""

FLY, SPIDER, BIRD, CAT, DOG, GOAT, COW, HORSE = 0, 1, 2, 3, 4, 5, 6, 7

first = "I know an old lady who swallowed a {}."
second = "I don't know how she swallowed a {}!"
third = "She swallowed the {} to catch the {}{}."
second = [
    "I don't know why she swallowed the fly. Perhaps she'll die.",
    "It wriggled and jiggled and tickled inside her.",
    "How absurd to swallow a bird!",
    "Imagine that, to swallow a cat!",
    "What a hog, to swallow a dog!",
    "Just opened her throat and swallowed a goat!",
    "I don't know how she swallowed a cow!",
    "She's dead, of course!",
]
animals = ["fly", "spider", "bird", "cat", "dog", "goat", "cow", "horse"]
extra = " that wriggled and jiggled and tickled inside her"


def create_verse(verse):
    animal = verse - 1
    response = [first.format(animals[animal]), second[animal]]
    if animal == HORSE:
        return response
    while animal:
        predator = animal - 1
        response.append(
            third.format(
                animals[animal],
                animals[predator],
                extra if predator == SPIDER else "",
            )
        )
        animal = predator
    if verse > 1:
        response.append(second[0])
    return response


def recite(start_verse, end_verse):
    verses = []
    for verse in range(start_verse, end_verse + 1):
        if verse > start_verse:
            verses.append("")
        verses.extend(create_verse(verse))

    return verses
