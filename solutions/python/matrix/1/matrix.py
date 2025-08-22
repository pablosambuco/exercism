class Matrix:
    def __init__(self, matrix_string: str):
        self.matrix = [
            [int(x) for x in line.split()] for line in matrix_string.splitlines()
        ]

    def row(self, index):
        return self.matrix[index - 1]

    def column(self, index):
        return [line[index - 1] for line in self.matrix]
