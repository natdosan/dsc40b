def mode(numbers):
    """
    Given an array of numbers, calculates the mode 
    in O(n) average time complexity

    Parameters
    ----------
    numbers : list
        array of nums (assumes acceptable input)

    Returns
    -------
    mode : int/float
        the mode of numbers
    """
    if len(numbers) == 0:
        raise ValueError("The input array should not be empty")

    frequency_dict = {}
    max_frequency = 0
    mode = None

    for number in numbers:
        if number in frequency_dict:
            frequency_dict[number] += 1
        else:
            frequency_dict[number] = 1

        if frequency_dict[number] > max_frequency:
            max_frequency = frequency_dict[number]
            mode = number

    return mode