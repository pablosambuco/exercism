# Discount improvement analysis
#
# ? 9 books:
#  group of 4 and 5
#!   4 x 20 + 5 x 25 = 205 => best discount
#  3 groups of 3
#    3 x 3 x 10 = 90       => worst
#
# ? 8 books:
#  group of 3 and 5
#    3 x 10 + 5 x 25 = 155 => worst
#  group of 4 and 4
#!   4 x 20 + 4 x 20 = 160 => best discount
#
# ? 7 books:
#  group of 2 and 5
#!   2 x 5 + 5 x 25 = 135  => best discount
#  group of 3 and 4
#    3 x 10 + 4 x 20 = 110 => worst
#
# ? 6 books:
#  group of 1 and 5
#!   1 x 0 + 5 x 25 = 125  => best discount
#  group of 2 and 4
#    2 x 5 + 4 x 20 = 90   => second
#  group of 3 and 3
#    3 x 10 + 3 x 10 = 60  => worst
#
#! Conclusion: the only improvement scenario is to change 5 + 3 for 4 + 4


PRICE = 8_00
DISCOUNTS = {
    0: 0.00,
    1: 0.00,
    2: 0.05,
    3: 0.10,
    4: 0.20,
    5: 0.25,
}


def total(basket):
    # sourcery skip: replace-dict-items-with-values, use-dict-items
    if not basket:
        return 0

    books = {}
    for book in basket:
        books[book] = books.get(book, 0) + 1

    groups = max(books.values())

    lengths = []
    for _ in range(groups):
        lengths.append(len([item for item in books if books[item] > 0]))
        for book in books:
            books[book] -= 1

    while 5 in lengths and 3 in lengths:
        for i in range(groups):
            if lengths[i] == 5:
                for j in range(groups):
                    if lengths[j] == 3:
                        lengths[i] -= 1
                        lengths[j] += 1
                        break

    return sum(x * PRICE * (1 - DISCOUNTS[x]) for x in lengths)
