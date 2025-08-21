import random


class Robot:
    uniquenames = []

    def __init__(self):
        self.name = self._getname()

    def reset(self):
        self.name = self._getname()

    @classmethod
    def _getname(cls):
        name = (
            chr(ord("A") + random.randint(0, 25))
            + chr(ord("A") + random.randint(0, 25))
            + f"{random.randint(000, 999):03}"
        )
        if name not in cls.uniquenames:
            cls.uniquenames.append(name)
            return name
        return cls._getname()
