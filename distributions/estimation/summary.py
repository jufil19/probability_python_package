import statistics
import pandas as pd


def summary(data):
    """Returns the minumum, maximum, mean, and variance of the provided data. 

    Args:
        data (list): List of observations

    Returns:
        dictionary with minimum value, maximum value, variance, and mean. 
    """
    variance = statistics.variance(data)
    mean = statistics.mean(data)

    return {"Min": min(data), "Max":max(data), "Variance":variance, "Mean": mean}


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