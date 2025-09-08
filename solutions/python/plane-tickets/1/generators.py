"""Functions to automate Conda airlines ticketing system."""


def generate_seat_letters(number):
    """Generate a series of letters for airline seats.

    :param number: int - total number of seat letters to be generated.
    :return: generator - generator that yields seat letters.

    Seat letters are generated from A to D.
    After D it should start again with A.

    Example: A, B, C, D

    """
    letters = ["A", "B", "C", "D"]
    for idx in range(number):
        yield letters[idx % 4]


def generate_row_numbers(number):
    """Generate row numbers

    :param number: int - total number of row numbers to be generated
    :return: generator - generator that yields row numbers

    There is no row 13.
    Each row has 4 seats.

    Args:
        number (_type_): _description_
    """
    numbers = [i + 1 for i in range(number // 4 + 1)]
    for idx in range(number):
        n = numbers[idx // 4]
        yield n if n < 13 else n + 1


def generate_seats(number):
    """Generate a series of identifiers for airline seats.

    :param number: int - total number of seats to be generated.
    :return: generator - generator that yields seat numbers.

    A seat number consists of the row number and the seat letter.

    There is no row 13.
    Each row has 4 seats.

    Seats should be sorted from low to high.

    Example: 3C, 3D, 4A, 4B

    """
    numbers = generate_row_numbers(number)
    letters = generate_seat_letters(number)
    for idx in range(number):
        yield f"{next(numbers)}{next(letters)}"


def assign_seats(passengers):
    """Assign seats to passengers.

    :param passengers: list[str] - a list of strings containing names of passengers.
    :return: dict - with the names of the passengers as keys and seat numbers as values.

    Example output: {"Adele": "1A", "Björk": "1B"}

    """
    seat = generate_seats(len(passengers))
    return {p: next(seat) for p in passengers}


def generate_codes(seat_numbers, flight_id):
    """Generate codes for a ticket.

    :param seat_numbers: list[str] - list of seat numbers.
    :param flight_id: str - string containing the flight identifier.
    :return: generator - generator that yields 12 character long ticket codes.

    """
    for seat in seat_numbers:
        yield f"{seat}{flight_id}".ljust(12,"0")
    
