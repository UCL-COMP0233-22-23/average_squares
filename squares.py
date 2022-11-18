"""Computation of weighted average of squares."""

#计算加权平方平均，默认所有数字权重相同，但可以通过list_of_weights更改
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
        assert len(list_of_weights) == len(list_of_numbers),\
            "weights and numbers must have same length"
        effective_weights = list_of_weights
    else:
        effective_weights = [1] * len(list_of_numbers)#结果是[1,1,1...]
    squares = [
        weight * number * number
        for number, weight
        in zip(list_of_numbers, effective_weights)
    ]
    return sum(squares)/len(list_of_numbers)

#将数字字符串转换为数字，忽略空格
def convert_numbers(list_of_strings):
    """Convert a list of strings into numbers, ignoring whitespace.
    
    Example:
    --------
    >>> convert_numbers(["4", " 8 ", "15 16", " 23    42 "])
    [4.0, 8.0, 15.0, 16.0, 23.0, 42.0]

    """
    all_numbers = []
    #append 和extend差不多，前者只能加一个
    for s in list_of_strings:
        # Take each string in the list, split it into substrings separated by
        # whitespace, and collect them into a single list...
        all_numbers.extend([token.strip() for token in s.split()])
    # ...then convert each substring into a number
    #将字符串转换为数字
    return [float(number_string) for number_string in all_numbers]


if __name__ == "__main__":
    numbers_strings = ["1","2","4"]
    weight_strings = ["1","1","1"]        
    
    numbers = convert_numbers(numbers_strings)
    weights = convert_numbers(weight_strings)
    
    result = average_of_squares(numbers, weights)
    
    print(result)
    
