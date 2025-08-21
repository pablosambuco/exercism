from random import choices

habilities = [
    "strength",
    "dexterity",
    "constitution",
    "intelligence",
    "wisdom",
    "charisma",
]


def modifier(value):
    return (value - 10) // 2


class Character:
    def __init__(self):
        self.strength = self.ability()
        self.dexterity = self.ability()
        self.constitution = self.ability()
        self.intelligence = self.ability()
        self.wisdom = self.ability()
        self.charisma = self.ability()
        self.hitpoints = 10 + modifier(self.constitution)

    def ability(self):
        dices = choices([1, 2, 3, 4, 5, 6], k=4)
        dices.remove(min(dices))
        return sum(dices)
