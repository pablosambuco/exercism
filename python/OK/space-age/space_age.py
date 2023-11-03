"""Space Age"""


class SpaceAge:
    """made with dicts :)"""
    year_lengths = {
        k: v * (365.25 * 24 * 60 * 60)
        for k, v in {
            "mercury": 0.2408467,
            "venus": 0.61519726,
            "earth": 1.0,
            "mars": 1.8808158,
            "jupiter": 11.862615,
            "saturn": 29.447498,
            "uranus": 84.016846,
            "neptune": 164.79132,
        }.items()
    }

    def __init__(self, seconds):
        self.seconds = seconds
        for planet, length in self.year_lengths.items():
            setattr(self, f"on_{planet}", self.calculate(length))

    def calculate(self, length):
        return lambda length=length: round(self.seconds / length, 2)
