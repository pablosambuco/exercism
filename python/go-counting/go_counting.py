WHITE = "W"
BLACK = "B"
NONE = " "


class Board:
    """Count territories of each player in a Go game

    Args:
        board (list[str]): A two-dimensional Go board
    """

    def __init__(self, board):
        self.board = board
        self.width = len(board[0])
        self.height = len(board)

    def is_correct_coordinate(self, x, y):
        return x in range(self.width) and y in range(self.height)

    def recursive_explore(self, x, y, territories=None):
        if self.board[y][x] in (WHITE, BLACK):
            return (self.board[y][x], set())

        if territories is None:
            territories = set()
        territories.add((x, y))

        owners = set([NONE])

        deltas = {
            "up   ": (+0, -1),
            "down ": (+0, +1),
            "left ": (-1, +0),
            "rigth": (+1, +0),
        }
        for delta in deltas.values():
            if (
                self.is_correct_coordinate(x + delta[0], y + delta[1])
                and (x + delta[0], y + delta[1]) not in territories
            ):
                stones, new_terr = self.recursive_explore(
                    x + delta[0], y + delta[1], territories
                )
                owners.update(stones)
                territories.update(new_terr)

        return owners, territories

    def territory(self, x, y) -> (str, set):
        """Find the owner and the territories given a coordinate on
           the board

        Args:
            x (int): Column on the board
            y (int): Row on the board

        Returns:
            (str, set): A tuple, the first element being the owner
                        of that area.  One of "W", "B", "".  The
                        second being a set of coordinates, representing
                        the owner's territories.
        """
        if not self.is_correct_coordinate(x, y):
            raise ValueError("Invalid coordinate")

        if self.board[y][x] in (WHITE, BLACK):
            return (NONE, set())

        owners, territories = self.recursive_explore(x, y)
        owners.remove(NONE)
        return (owners.pop() if len(owners) == 1 else NONE, territories)

    def territories(self):
        """Find the owners and the territories of the whole board

        Args:
            none

        Returns:
            dict(str, set): A dictionary whose key being the owner
                        , i.e. "W", "B", "".  The value being a set
                        of coordinates owned by the owner.
        """
        all_territories = {
            WHITE: set(),
            BLACK: set(),
            NONE: set(),
        }
        for i in range(self.width):
            for j in range(self.height):
                stone, territories = self.territory(i, j)
                all_territories[stone].update(territories)
        return all_territories
