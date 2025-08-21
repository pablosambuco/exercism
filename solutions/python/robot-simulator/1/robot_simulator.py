# Globals for the directions
# Change the values as you see fit
EAST = 3
NORTH = 2
WEST = 1
SOUTH = 0

step = {
    EAST: (1, 0),
    NORTH: (0, 1),
    WEST: (-1, 0),
    SOUTH: (0, -1),
}


class Robot:
    def __init__(self, direction=NORTH, x_pos=0, y_pos=0):
        self.direction = direction
        self.coordinates = (x_pos, y_pos)

    def turn_left(self):
        self.direction = (self.direction - 1) % 4

    def turn_right(self):
        self.direction = (self.direction + 1) % 4

    def advance(self):
        self.coordinates = (
            self.coordinates[0] + step[self.direction][0],
            self.coordinates[1] + step[self.direction][1],
        )

    def move(self, instructions):
        inst = {
            "A": self.advance,
            "L": self.turn_left,
            "R": self.turn_right,
        }
        for letter in instructions:
            inst[letter]()
