class Move:
    def __init__(self, y, x):
        self.y = y
        self.x = x


class Queen:

    valid_moves = [Move(y, x) for x in [0, 1, -1] for y in [0, 1, -1]]

    def __init__(self, row, column):
        if row < 0:
            raise ValueError("row not positive")
        if row > 7:
            raise ValueError("row not on board")
        if column < 0:
            raise ValueError("column not positive")
        if column > 7:
            raise ValueError("column not on board")

        self.row = row
        self.column = column

    def is_at(self, row, column):
        return self.row == row and self.column == column

    def can_attack(self, other: "Queen"):
        if self.row == other.row and self.column == other.column:
            raise ValueError("Invalid queen position: both queens in the same square")

        for i in range(7):
            for move in Queen.valid_moves:
                if other.is_at(self.row + move.y * i, self.column + move.x * i):
                    return True

        return False
