class Card:
    letter_values = {"A": 14, "K": 13, "Q": 12, "J": 11}

    def __init__(self, card):
        self.suit = card[-1]
        self.number = card[:-1]
        self.value = (
            Card.letter_values[self.number]
            if self.number in Card.letter_values
            else int(self.number)
        )

    def __str__(self):
        return self.number + self.suit

    def __lt__(self, other):
        return self.value < other.value


class Hand:
    (
        CARDS,
        PAIR,
        DOUBLE_PAIR,
        THREE_OF_A_KIND,
        STRAIGHT,
        FLUSH,
        FULL_HOUSE,
        POKER,
        STRAIGHT_FLUSH,
    ) = (10**i for i in range(9))

    def __init__(self, hand):
        self.cards = [Card(card) for card in hand.split(" ")]
        self.games = self.identify_games()

    def __str__(self):
        return " ".join(map(str, self.cards))

    def __lt__(self, other):
        return self.value() < other.value()

    def identify_games(self):  # sourcery skip: remove-dict-keys
        values = sorted([card.value for card in self.cards], reverse=True)
        suits = [card.suit for card in self.cards]

        games = {
            Hand.STRAIGHT_FLUSH: [],
            Hand.POKER: [],
            Hand.FULL_HOUSE: [],
            Hand.FLUSH: [],
            Hand.STRAIGHT: [],
            Hand.THREE_OF_A_KIND: [],
            Hand.DOUBLE_PAIR: [],
            Hand.PAIR: [],
            Hand.CARDS: [],
        }

        value_count = {}
        for value in values:
            value_count[value] = value_count.get(value, 0) + 1

        for value, count in value_count.items():
            if count == 1:
                games[Hand.CARDS].append(value)
            if count == 2:
                games[Hand.PAIR].append(value)
            if count == 3:
                games[Hand.THREE_OF_A_KIND].append(value)
            if count == 4:
                games[Hand.POKER].append(value)

        suit_count = {}
        for suit in suits:
            suit_count[suit] = suit_count.get(suit, 0) + 1

        if 5 in suit_count.values():
            games[Hand.FLUSH].extend(values)

        if all(values[i] - 1 == values[i + 1] for i in range(4)):
            games[Hand.STRAIGHT].extend(values)
            games[Hand.CARDS] = []
        
        if values[0] == 14 and all(values[i + 1] - 1 == values[i + 2] for i in range(3)) and values[4] == 2:
            values.remove(14)
            values.append(1)
            games[Hand.STRAIGHT].extend(values)
            games[Hand.CARDS] = []

        if len(games[Hand.PAIR]) == 2:
            games[Hand.DOUBLE_PAIR] = games[Hand.PAIR]
            games[Hand.PAIR] = []

        if games[Hand.PAIR] and games[Hand.THREE_OF_A_KIND]:
            games[Hand.FULL_HOUSE].extend(games[Hand.THREE_OF_A_KIND])
            games[Hand.FULL_HOUSE].extend(games[Hand.PAIR])
            games[Hand.PAIR] = []
            games[Hand.THREE_OF_A_KIND] = []

        if games[Hand.FLUSH] and games[Hand.STRAIGHT]:
            games[Hand.STRAIGHT_FLUSH].extend(games[Hand.STRAIGHT])
            games[Hand.FLUSH] = []
            games[Hand.STRAIGHT] = []

        for game in list(games.keys()):
            if not games[game]:
                del games[game]

        return games

    def value(self):
        return list(self.games.items())


def best_hands(hands):
    hands = [Hand(hand) for hand in hands]

    for hand in hands:
        print(hand, hand.value())

    max_value = max(hand.value() for hand in hands)
    return [str(hand) for hand in hands if hand.value() == max_value]
