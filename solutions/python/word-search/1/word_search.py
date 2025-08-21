class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __repr__(self):
        return f"Point({self.x},{self.y})"


class WordSearch:
    def __init__(self, puzzle):
        self.puzzle = puzzle
        self.height = len(puzzle) if puzzle else 0
        self.width = len(puzzle[0]) if puzzle else 0

    def in_board(self, x, y):
        return x in range(self.width) and y in range(self.height)

    def search(self, word):
        for i in range(self.width):
            for j in range(self.height):
                if self.puzzle[j][i] == word[0]:
                    start = Point(i, j)
                    print(start)
                    if start:
                        end = self.find_end(start, word)
                        print(end)
                        if end:
                            return start, end
        return None

    def find_end(self, start, word):
        deltas = [
            (+0, +1),  # Horizontal Left to Right
            (+0, -1),  # Horizontal Right to Left
            (+1, +0),  # Vertical Top-Down
            (-1, +0),  # Vertical Bottom-Up
            (+1, +1),  # Diagonal Top-Left to Bottom-Right
            (+1, -1),  # Diagonal Top-Right to Bottom-Left
            (-1, +1),  # Diagonal Bottom-Left to Top-Right
            (-1, -1),  # Diagonal Bottom-Right to Top-Left
        ]
        len_word = len(word)
        for delta in deltas:
            i, j = start.x, start.y
            k = 1
            while self.in_board(i + delta[0], j + delta[1]) and k < len_word:
                i += delta[0]
                j += delta[1]
                if self.puzzle[j][i] != word[k]:
                    break
                k += 1
            if k == len_word:
                return Point(i, j)
        return None
