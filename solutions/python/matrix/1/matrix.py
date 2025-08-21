class Matrix:
    def __init__(self, matrix_string: str):
        lines = matrix_string.splitlines()
        self.rows = [[int(x) for x in line.split()] for line in lines]
        self.columns = [
            [self.rows[j][i] for j in range(len(lines))]
            for i in range(len(self.rows[0]))
        ]

    def row(self, index):
        return self.rows[index - 1]

    def column(self, index):
        return self.columns[index - 1]
