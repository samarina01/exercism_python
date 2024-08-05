"""Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language:
https://en.wikipedia.org/wiki/Guido_van_Rossum

This is a module docstring, used to describe the functionality
of a module and its functions and/or classes.
"""


#TODO: define the 'EXPECTED_BAKE_TIME' constant.
EXPECTED_BAKE_TIME = 40

#TODO: Remove 'pass' and complete the 'bake_time_remaining()' function below.
def bake_time_remaining(elapsed_baked_time):
    """Calculate the bake time remaining.

        :param elapsed_bake_time: int - baking time already elapsed.
        :return: int - remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.

        Function that takes the actual minutes the lasagna has been in the oven as
        an argument and returns how many minutes the lasagna still needs to bake
        based on the `EXPECTED_BAKE_TIME`.
        """
    EXPECTED_BAKE_TIME = 40
    remaining_bake_time = EXPECTED_BAKE_TIME - elapsed_baked_time

    return remaining_bake_time


#TODO: Define the 'preparation_time_in_minutes()' function below.
# You might also consider using 'PREPARATION_TIME' here, if you have it defined.
def preparation_time_in_minutes(number_of_layers):
    """Calculate the cooking preparation time.

    :param number_of_layers: int - the number of layers in the lasagna.
    :return: int - total time (in minutes) preparing.

    This function takes one integer representing the number of lasagna layers
    and calculates the total minutes spent preparing the lasagna.
    """
    preparation_time = 0
    preparation_time = number_of_layers * 2

    return preparation_time


#TODO: define the 'elapsed_time_in_minutes()' function below.
# Remember to add a docstring (you can copy and then alter the one from bake_time_remaining.)
def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """Calculate the elapsed cooking time.

    :param number_of_layers: int - the number of layers in the lasagna.
    :param elapsed_bake_time: int - elapsed cooking time.
    :return: int - total time elapsed (in minutes) preparing and cooking.

    This function takes two integers representing the number of lasagna layers and the
    time already spent baking and calculates the total elapsed minutes spent cooking the
    lasagna.
    """
    elapsed_time = number_of_layers*2 + elapsed_bake_time

    return elapsed_time