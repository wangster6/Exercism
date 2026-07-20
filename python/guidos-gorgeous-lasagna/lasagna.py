"""Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language:
https://en.wikipedia.org/wiki/Guido_van_Rossum

This is a module docstring, used to describe the functionality
of a module and its functions and/or classes.
"""


EXPECTED_BAKE_TIME = 40
PREPARATION_TIME = 2


def bake_time_remaining(elapsed_bake_time):
    """Calculate the bake time remaining.

    Parameters:
        elapsed_bake_time (int): The baking time already elapsed.

    Returns:
        int: The remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """

    return EXPECTED_BAKE_TIME - elapsed_bake_time

def preparation_time_in_minutes(number_of_layers):
    """Calculate the amount of time needed (in minutes)to prepare a certain number of layers.

    Parameters:
        number_of_layers (int): The number of layers you want to add to the lasagna.

    Returns:
        int: How many minutes it would take to prepare the additional layers of lasagna.

    Function that takes the number of additional layers to add to the lasagna and
    returns how many minutes the it would take to prep those layers based on the
    `PREPARATION_TIME`.
    """
    return number_of_layers * PREPARATION_TIME


def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """Calculate the total minutes you have been in the kitchen

    Parameters:
        number_of_layers (int): The number of layers you want to add to the lasagna.
        elapsed_bake_time (int): The baking time already elapsed.

    Returns:
        int: The total minutes you have been in the kitchen cooking — your preparation time layering + the time the lasagna has spent baking in the oven.
    
    Function that takes the number of additional layers to add to the lasagna and
    returns how many minutes the it would take to prep those layers based on the
    `PREPARATION_TIME`. It then takes that time and adds it onto the baking time already elapsed.
    """
    return preparation_time_in_minutes(number_of_layers) + elapsed_bake_time