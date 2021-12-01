import statistics
import pandas as pd


def summary(data):
    """Prints the minumum, maximum, mean, and variance of the provided data. 

    Args:
        data (list): List of observations

    Returns:
        None
    """
    print(f"Minimum value: {min(data)}")
    print(f"Maximum value: {max(data)}")
    print(f"Variance: {statistics.variance(data)}")
    print(f"Mean: {statistics.mean(data)}")


def contains_all_ints(data):
    """Determines whether the data contains only integers. 

    Args:
        data (list): List of observations

    Returns:
        (bool): whether or not the list is entirely composed of integers. 
    """
    for i in data:
        if isinstance(i, int) == False:
            return False
    return True

def is_non_negative(data):
    """Determines whether the data contains only non-negative values. 

    Args:
        data (list): List of observations

    Returns:
        (bool): whether or not the list is entirely composed of non-negative numbers. 
    """
    for i in data:
        if i < 0:
            return False
    return True