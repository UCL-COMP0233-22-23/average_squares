"""Computation of weighted average of squares."""
from argparse import ArgumentParser

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
    return sum(squares)/ len(squares)


def convert_numbers(list_of_strings):
    """Convert a list of strings into numbers, ignoring whitespace.
    
    Example:
    --------
    >>> convert_numbers(["4", " 8 ", "15 16", " 23    42 "])
    [4.0, 8.0, 15.0, 16.0, 23.0, 42.0]

    """
    all_numbers = []
    for s in list_of_strings:
        # Take each string in the list, split it into substrings separated by
        # whitespace, and collect them into a single list...
        all_numbers.extend([token.strip() for token in s.split()])
    # ...then convert each substring into a number
    return [float(number_string) for number_string in all_numbers]


def process():
    parser = ArgumentParser(description="Computation of weighted average of squares.")

    parser.add_argument('numbers_strings')
    parser.add_argument('--weight_strings', '-w')

    arguments = parser.parse_args()

    if arguments.weight_strings:
        result = average_of_squares(convert_numbers(arguments.numbers_strings), convert_numbers(arguments.weight_strings))
    else:
        result = average_of_squares(convert_numbers(arguments.numbers_strings))
    print(result)

def process_file():
    parser = ArgumentParser(description="Computation of weighted average of squares.")

    parser.add_argument('numbers_file')
    parser.add_argument('--weight_file', '-w')

    arguments = parser.parse_args()

    with open(arguments.numbers_file, 'r') as f:
        numbers = f.readline()

    if arguments.weight_file:
        with open(arguments.weight_file, 'r') as f:
            weights = f.readline()
        result = average_of_squares(convert_numbers(numbers), convert_numbers(weights))
    else:
        result = average_of_squares(convert_numbers(numbers))

    print(result)
if __name__ == "__main__":
    process_file()