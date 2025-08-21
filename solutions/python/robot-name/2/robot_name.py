import random


class Robot:
    uniquenames = ["DUMMY"]

    def __init__(self):
        self.name = self._getname()

    def reset(self):
        self.name = self._getname()

    @classmethod
    def _getname(cls):
        random.seed("excercism robot name")
        name = "DUMMY"
        while name in cls.uniquenames:
            name = (
                chr(ord("A") + random.randint(0, 25))
                + chr(ord("A") + random.randint(0, 25))
                + f"{random.randint(000, 999):03}"
            )
        cls.uniquenames.append(name)
        return name

