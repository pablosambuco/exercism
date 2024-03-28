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
    dice.sort()
    d1 = dice[0]
    d2 = dice[1]
    d3 = dice[2]
    d4 = dice[3]
    d5 = dice[4]

    if category in (ONES, TWOS, THREES, FOURS, FIVES, SIXES):
        return category*dice.count(category)
    if category == FULL_HOUSE:
        return sum(dice) if dice.count(d1) == 3 and dice.count(d5) == 2 or dice.count(d1) == 2 and dice.count(d5) == 3 else 0
    if category == FOUR_OF_A_KIND:
        return 4 * d3 if d1 == d2 == d3 == d4 or d2 == d3 == d4 == d5 else 0
    if category == LITTLE_STRAIGHT:
        return 30 if dice == [1,2,3,4,5] else 0
    if category == BIG_STRAIGHT:
        return 30 if dice == [2,3,4,5,6] else 0
    if category == CHOICE:
        return sum(dice)
    if category == YACHT:
        return 50 if d1 == d2 == d3 == d4 == d5 else 0

    return 0
