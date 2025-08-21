from random import choices

abilities = [
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
        for ability in abilities:
            setattr(self, ability, self.ability())
        self.hitpoints = 10 + modifier(self.constitution)

    def ability(self):
        dices = sorted(choices([1, 2, 3, 4, 5, 6], k=4))
        return sum(dices[1:])
