from pprint import pprint

PLAYER1 = "O"
PLAYER2 = "X"


class Board:
    def __init__(self, text: str):
        self.cells = []
        for line in text.splitlines():
            row = list(line.replace(" ", ""))
            self.cells.append(row)
        print(text)
        self.width = len(self.cells[0])
        self.heigth = len(self.cells)

    def get_cell(self, i, j):
        return self.cells[j][i]

    def get_neighbors(self, x, y):
        displacements = [
            (-1, +0),
            (+1, +0),
            (+0, -1),
            (+1, -1),
            (-1, +1),
            (+0, +1),
        ]
        print(x, y)
        possibles = [
            (x + i, y + j)
            for i, j in displacements
            if 0 <= x + i < self.width and 0 <= y + j < self.heigth
        ]

        print(possibles)
        return possibles

    def get_free_neighbors(self, x, y, visited):
        neighbors = self.get_neighbors(x, y)
        following = [cell for cell in neighbors if cell not in visited]
        print(following)
        return following

    def get_next_cell(self, cell, player, path, discarded):
        new_path = path
        new_discarded = discarded
        options = self.get_free_neighbors(cell[0], cell[1], path + discarded)
        for new_cell in options:
            if self.get_cell(new_cell[0], new_cell[1]) != player:
                print("descartada", new_cell)
                new_discarded.append(new_cell)
            else:
                print("probando", new_cell)
                new_path, new_discarded = self.get_next_cell(
                    new_cell, player, new_path + [new_cell], new_discarded
                )
        return new_path, new_discarded


class ConnectGame:
    def __init__(self, text):
        self.board = Board(text)

    def get_winner(self):
        path = []
        discarded = []
        player = PLAYER1
        for i in range(self.board.width):
            if self.board.get_cell(i, 0) == player:
                path.append((i, 0))
                path, discarded = self.board.get_next_cell(
                    (i, 0), player, path, discarded
                )

        for i in range(self.board.width):
            if (i, self.board.heigth - 1) in path:
                return player

        path = []
        discarded = []
        player = PLAYER2
        for j in range(self.board.heigth):
            if self.board.get_cell(0, j) == player:
                path.append((0, j))
                path, discarded = self.board.get_next_cell(
                    (0, j), player, path, discarded
                )
        for j in range(self.board.heigth):
            if (self.board.width - 1, j) in path:
                return player

        return ""
