"""Computation of weighted average of squares."""


def average_of_squares(list_of_numbers, list_of_weights=None):
    """ Return the weighted average of a list of values.
    
    By default, all values are equally weighted, but this can be changed
    by the list_of_weights argument.
    
    Example:
    --------
    >>> average_of_squares([1, 2, 4])
    7.0
    >>> average_of_squares([2, 4], [1, 0.5])
    6.0
    >>> average_of_squares([1, 2, 4], [1, 0.5])
    Traceback (most recent call last):
    AssertionError: weights and numbers must have same length

    """
    if list_of_weights is not None:
        assert len(list_of_weights) == len(list_of_numbers), \
            "weights and numbers must have same length"
        effective_weights = list_of_weights
    else:
        effective_weights = [1] * len(list_of_numbers)
    squares = [
        weight * number * number
        for number, weight
        in zip(list_of_numbers, effective_weights)
    ]
    return sum(squares)/len(list_of_numbers)


def convert_numbers(list_of_strings):
    """Convert a list of strings into numbers, ignoring whitespace.
    
    Example:
    --------
    >>> convert_numbers(["4", " 8 ", "15 16"])
    [4, 8, 15, 16]

    """
    all_numbers = []
    for s in list_of_strings:
        # Take each string in the list, split it into substrings separated by
        # whitespace, and collect them into a single list...
        all_numbers.extend([token.strip() for token in s.split()])
    # ...then convert each substring into a number
    return [int(number_string) for number_string in all_numbers]



from argparse import ArgumentParser
import os.path
from os import path

if __name__ == "__main__":
    #numbers_strings = ["1","2","4"]
    #weight_strings = ["1","1","1"]        

    #numbers = convert_numbers(numbers_strings)


    parser = ArgumentParser()
    parser.add_argument('numbers_strings')
    parser.add_argument('--weights', '-w')
    arguments = parser.parse_args()    
    



    if  path.exists(arguments.numbers_strings) == True:

        with open(arguments.numbers_strings, 'r') as f: #open file
            numbers_strings = str( f.readline() ) #read and get numbers as strings from file
            numbers = convert_numbers(numbers_strings)

    else:        
        numbers = convert_numbers(arguments.numbers_strings)




    if  path.exists(arguments.weights) == True:
        with open(arguments.weights, 'r') as f: #open file
            weights_strings = str( f.readline() ) #read and get numbers as strings from file
            weights_strings = convert_numbers(weights_strings)

    else:
        weights = convert_numbers(arguments.weights)
        



    result = average_of_squares(numbers, weights)

    print(result)