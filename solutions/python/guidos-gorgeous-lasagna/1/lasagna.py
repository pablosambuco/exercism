"""Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language:
https://en.wikipedia.org/wiki/Guido_van_Rossum
"""

EXPECTED_BAKE_TIME=40
PREPARATION_TIME=2

def bake_time_remaining(elapsed_bake_time):
    """Calculate the bake time remaining.

    :param elapsed_bake_time: int - baking time already elapsed.
    :return: int - remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """

    if EXPECTED_BAKE_TIME > elapsed_bake_time:
        return EXPECTED_BAKE_TIME - elapsed_bake_time
    return 0


def preparation_time_in_minutes(layers):
    """Returns the preparation time.
    :param: int - layers

    :return: int - preparation time (in minutes) derived from 'PREPARATION_TIME'.

    Function that returns how many minutes the lasagna takes to be prepared
    based on the PREPARATION_TIME.
    """

    return layers*PREPARATION_TIME

#TODO: define the 'elapsed_time_in_minutes()' function below.
# Remember to add a docstring (you can copy and then alter the one from bake_time_remaining.)

def elapsed_time_in_minutes(layers,elapsed):
    """Returns the elapsed time.

    :return: int - elapsed time (in minutes).

    Function that returns something.
    """

    return preparation_time_in_minutes(layers)+elapsed
