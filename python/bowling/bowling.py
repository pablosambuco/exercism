MIN_PINS = 0
MAX_PINS = 10
MAX_FRAMES = 10
STRIKE = 10


class BownlingFrame:
    def __init__(self, length):
        self.frame = [None] * length

    def __getitem__(self, pos):
        return self.frame[pos]

    def __setitem__(self, pos, value):
        self.frame[pos] = value

    @property
    def is_empty(self):
        return self.frame[0] is None

    @property
    def spare_empty(self):
        return self.frame[1] is None

    @property
    def bonus_empty(self):
        return self.frame[2] is None

    @property
    def is_strike(self):
        return self.frame[0][0] == MAX_PINS

    @property
    def is_last(self):
        return len(self.frame) == 3

    @property
    def is_spare(self):
        return self.frame[0][0] + self.frame[1][0] == MAX_PINS

    @property
    def roll(self):
        return self.frame[0][1]

    @property
    def spare_value(self):
        return self.frame[0][0] + self.frame[1][0]

    def bad_spare(self, pins):
        return self.frame[0][0] + pins > MAX_PINS

    def bad_bonus(self, pins):
        return self.frame[1][0] < MAX_PINS and self.frame[1][0] + pins > MAX_PINS


class BowlingGame:
    def __init__(self):
        # nine 2-roll frames and one 3-roll frame at the end
        self.frames = []
        self.rolls = []
        self.add_frame()
        self.running = True

    def add_frame(self):
        if len(self.frames) == MAX_FRAMES - 1:
            self.frames.append(BownlingFrame(3))
        else:
            self.frames.append(BownlingFrame(2))

    def roll(self, pins):
        frame = self.frames[-1]
        roll = (pins, len(self.rolls))
        self.rolls.append(pins)

        if not self.running:
            raise ValueError("Invalid frame")
        if not MIN_PINS <= pins <= MAX_PINS:
            raise ValueError("Pins cannot be negative or more than 10")

        if frame.is_last:
            if frame.is_empty:
                frame[0] = roll
            elif frame.spare_empty:
                frame[1] = roll
                if frame.spare_value < MAX_PINS:
                    self.running = False
            else:
                if frame.is_strike and frame.bad_bonus(pins):
                    raise ValueError("There shouldn't be more than 10 pins")
                frame[2] = roll
                self.running = False
        else:
            if pins == STRIKE:
                frame[0] = roll
                self.add_frame()
            else:
                if frame.is_empty:
                    frame[0] = roll
                else:
                    if frame.bad_spare(pins):
                        raise ValueError("There shouldn't be more than 10 pins")
                    frame[1] = roll
                    self.add_frame()

    def score(self):
        if len(self.frames) < MAX_FRAMES:
            raise Exception("Incomplete game")
        if len(self.frames) == MAX_FRAMES:
            last = self.frames[-1]
            if (
                last.is_empty
                or (last.is_strike and (last.spare_empty or last.bonus_empty))
                or (last.is_spare and last.bonus_empty)
            ):
                raise Exception("Incomplete game")

        result = 0
        for i in range(len(self.frames)):
            frame = self.frames[i]
            roll = frame.roll
            if frame.is_strike or frame.is_spare:
                result += sum(self.rolls[roll : roll + 3])
            else:
                result += sum(self.rolls[roll : roll + 2])
        return result
