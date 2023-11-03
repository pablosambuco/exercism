import itertools
ocr_data = {
    "     |  |   ": "1",
    " _  _||_    ": "2",
    " _  _| _|   ": "3",
    "   |_|  |   ": "4",
    " _ |_  _|   ": "5",
    " _ |_ |_|   ": "6",
    " _   |  |   ": "7",
    " _ |_||_|   ": "8",
    " _ |_| _|   ": "9",
    " _ | ||_|   ": "0",
}


def convert(input_grid):
    rows = len(input_grid)
    columns = len(input_grid[0])

    if rows % 4 != 0:
        raise ValueError("Number of input lines is not a multiple of four")

    if columns % 3 != 0:
        raise ValueError("Number of input columns is not a multiple of three")

    answer = ""
    for base_row in range(0, rows, 4):
        if answer:
            answer += ","
        for base_column in range(0, columns, 3):
            aux = "".join(
                input_grid[base_row + row][base_column + column]
                for row, column in itertools.product(range(4), range(3))
            )
            answer += ocr_data.get(aux, "?")
    return answer
