# Score categories.
# Change the values as you see fit.
YACHT = 0
ONES = 1
TWOS = 2
THREES = 3
FOURS = 4
FIVES = 5
SIXES = 6
FULL_HOUSE = 7
FOUR_OF_A_KIND = 8
LITTLE_STRAIGHT = 9
BIG_STRAIGHT = 10
CHOICE = 11


def score(dice, category):
    d1 = dice[0]
    d2 = dice[1]
    d3 = dice[2]
    d4 = dice[3]
    d5 = dice[4]

    if category in (ONES, TWOS, THREES, FOURS, FIVES, SIXES):
        return (
            category if d1 == category else 0
            + category if d2 == category else 0
            + category if d3 == category else 0
            + category if d4 == category else 0
            + category if d5 == category else 0
        )
    if category == FULL_HOUSE:
        return 0
    if category == FOUR_OF_A_KIND:
        return 0
    if category == LITTLE_STRAIGHT:
        return 30 if dice.sort() == [1,2,3,4,5] else 0
    if category == BIG_STRAIGHT:
        return 30 if dice.sort() == [2,3,4,5,6] else 0
    if category == CHOICE:
        return sum(dice)
    if category == YACHT:
        return 50 if d1 == d2 == d3 == d4 == d5 else 0

    return 0
