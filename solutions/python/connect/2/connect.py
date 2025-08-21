PLAYER1 = "O"
PLAYER2 = "X"


class Board:
    def __init__(self, text: str):
        self.cells = [list(line.replace(" ", "")) for line in text.splitlines()]
        self.width = len(self.cells[0])
        self.height = len(self.cells)
        self.displacements = [(-1, 0), (1, 0), (0, -1), (1, -1), (-1, 1), (0, 1)]

    def get_cell(self, i, j):
        return self.cells[j][i]

    def get_next_cell(self, cell, player, path: set):
        stack = [cell]
        while stack:
            cell = stack.pop()
            for i, j in self.displacements:
                if 0 <= cell[0] + i < self.width and 0 <= cell[1] + j < self.height:
                    new_cell = (cell[0] + i, cell[1] + j)
                    if (
                        new_cell not in path
                        and self.cells[new_cell[1]][new_cell[0]] == player
                    ):
                        path.add(new_cell)
                        stack.append(new_cell)
        return path

    def transpose(self):
        self.width, self.height = self.height, self.width
        self.cells = list(zip(*self.cells))


class ConnectGame:
    def __init__(self, text):
        self.board = Board(text)

    def get_winner(self):
        if self.check_winner(PLAYER1):
            return PLAYER1
        self.board.transpose()
        if self.check_winner(PLAYER2):
            return PLAYER2
        return ""

    def check_winner(self, player):
        path = set()
        for i in range(self.board.width):
            if self.board.cells[0][i] == player:
                path.add((i, 0))
                path = self.board.get_next_cell((i, 0), player, path)
        for i in range(self.board.width):
            if (i, self.board.height - 1) in path:
                return True
        return False
