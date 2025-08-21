class Clock:
    def __init__(self, hour, minute):
        self.hour, self.minute = Clock.fix(hour, minute)

    def __repr__(self):
        return f"Clock({self.hour}, {self.minute})"

    def __str__(self):
        return f"{self.hour:02}:{self.minute:02}"

    def __eq__(self, other):
        return self.hour == other.hour and self.minute == other.minute

    def __add__(self, minutes):
        self.hour, self.minute = Clock.fix(self.hour, self.minute + minutes)
        return self

    def __sub__(self, minutes):
        return self.__add__(-minutes)

    @staticmethod
    def fix(hour, minute):
        hour += minute // 60
        return hour % 24, minute % 60
