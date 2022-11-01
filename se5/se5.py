"""
CAPP 121 Short Exercises #5
"""

import numpy as np

def reshape_array(x, new_dims):
    """
    Create a new 2-dimensional array with the values of x, if possible

    Inputs:
        x (array): 2-dimensional array
        new_dims (2-tuple of int): the number of rows and number of columns
          in the output array

    Returns (array): A new 2-dimensional array with new_dims, or x
    """
    # YOUR CODE HERE
    # Replace None with an appropriate return value
    return None


def harmonic_sequence(N):
    """
    Sum the first N values of the harmonic sequence: 1 + 1/2 + 1/3 + ... + 1/N

    Inputs:
        N (int): the number of values to sum

    Returns (float): The sum
    """
    # YOUR CODE HERE
    # Replace None with an appropriate return value
    return None


def clip_in_range(x, lb, ub):
    """
    Modify an array so that all values are between lb and ub inclusive

    Inputs:
        x (array): n-dimensional array
        lb (int or float): the lower bound
        ub (int or float): the upper bound

    Returns (None): Nothing, modifies x in-place 
    """
    # YOUR CODE HERE


def fill_missing_data(x):
    """
    Fill missing data (signaled by the value -1) with the mean of the array

    Inputs:
        x (array): n-dimensional array

    Returns (None): Nothing, modifies x in-place
    """
    # YOUR CODE HERE


def smallest_span(x):
    """
    Find the row with the smallest span of values, where the span of a row
        is the largest value in the row minus the smallest value

    Inputs:
        x (array): 2-dimensional array 

    Returns (int): The index of the row with the smallest span
    """
    # YOUR CODE HERE
    # Replace None with an appropriate return value
    return None


def select_row_col(x, rows=None, cols=None):
    """
    Select a subset of rows and columns in a 2-dimensional array

    Inputs:
        x (array): 2-dimensional array 
        rows (list of ints): a list of row index we are selecting, None if not specified
        cols (list of ints): a list of column index we are selecting, None if not specified

    Returns: a 2-dimensional array with the specified rows and cols
    """
    # YOUR CODE HERE
    # Replace None with an appropriate return value
    return None