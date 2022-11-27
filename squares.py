from argparse import ArgumentParser

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
    return sum(squares)/len(squares)


def convert_numbers(list_of_strings):
    """Convert a list of strings into numbers, ignoring whitespace.
    
    Example:
    --------
    >>> convert_numbers(["4", " 8 ", "15 16", " 23    42 "])
    [4, 8, 15, 16, 23, 42]

    """
    all_numbers = []
    for s in list_of_strings:
        # Take each string in the list, split it into substrings separated by
        # whitespace, and collect them into a single list...
        all_numbers.extend([token.strip() for token in s.split()])
    # ...then convert each substring into a number
    return [int(number_string) for number_string in all_numbers]


if __name__ == "__main__":
    parser = ArgumentParser(description="Generate correct averaged sums.")
    parser.add_argument('--file_numbers')
    parser.add_argument('--file_weights',default = 'default_weights.txt')    
    arguments= parser.parse_args()    
    
    with open(arguments.file_numbers,'r') as input_numbers:
        numbers = convert_numbers(input_numbers.readlines())

    with open(arguments.file_weights,'r') as input_weights:
        if input_weights!=None:
            weights = convert_numbers(input_weights.readlines())
        else:
            with open('default_weights.txt','r') as default_weights:
                weights = convert_numbers(default_weights.readlines())
    
    result = average_of_squares(numbers, weights)
    
    print(result)