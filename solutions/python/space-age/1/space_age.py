"""Space Age"""

EARTH_YEAR_SECONDS = 31557600
EARTH_TO_MERCURY = 0.2408467
EARTH_TO_VENUS = 0.61519726
EARTH_TO_EARTH = 1.0
EARTH_TO_MARS = 1.8808158
EARTH_TO_JUPITER = 11.862615
EARTH_TO_SATURN = 29.447498
EARTH_TO_URANUS = 84.016846
EARTH_TO_NEPTUNE = 164.79132


class SpaceAge:
    planet_relation = {}

    def __init__(self, seconds):
        self.seconds = seconds

    def on_mercury(self):
        return round(self.seconds / (EARTH_YEAR_SECONDS * EARTH_TO_MERCURY), 2)

    def on_venus(self):
        return round(self.seconds / (EARTH_YEAR_SECONDS * EARTH_TO_VENUS), 2)

    def on_earth(self):
        return round(self.seconds / (EARTH_YEAR_SECONDS * EARTH_TO_EARTH), 2)

    def on_mars(self):
        return round(self.seconds / (EARTH_YEAR_SECONDS * EARTH_TO_MARS), 2)

    def on_jupiter(self):
        return round(self.seconds / (EARTH_YEAR_SECONDS * EARTH_TO_JUPITER), 2)

    def on_saturn(self):
        return round(self.seconds / (EARTH_YEAR_SECONDS * EARTH_TO_SATURN), 2)

    def on_uranus(self):
        return round(self.seconds / (EARTH_YEAR_SECONDS * EARTH_TO_URANUS), 2)

    def on_neptune(self):
        return round(self.seconds / (EARTH_YEAR_SECONDS * EARTH_TO_NEPTUNE), 2)
