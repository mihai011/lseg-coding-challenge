"""_
Utils module function
"""

import numpy as np


def init(shape):
    """
    Initialize a numpy array of zeroes with the given shape.

    Args:
        shape (tuple): dimensions for the

    Returns:
        np.array: numpy array of zeroes
    """

    return np.zeros(shape, int)


def ones(area):
    """
    Initialize a numpy array of ones with the same shape as area parameter.

    Args:
        area (np.array): area of work

    Returns:
        np.array: numpy array of ones
    """

    return np.ones(area.shape)


def zeros(area):
    """
    Initialize a numpy array of zeros with the same shape as area parameter.
    Args:
        area (np.array): area of work

    Returns:
        np.array: numpy array of zeros
    """

    return np.zeros(area.shape)


def toogle(area):
    """
    Toggles values in an numpy array between 0 and 1.

    Args:
        area (np.array): area of work

    Returns:
        np.array: toggled numpy array
    """

    toogle_func = np.vectorize(lambda x: 1 - x)
    return np.apply_along_axis(toogle_func, 1, area)


def increase(area, amount):
    """
    Increases values in an numpy array by amount.

    Args:
        area (np.array): area of work
        amount (int): amount by which we increase

    Returns:
        np.array: increased numpy array
    """

    inc_func = np.vectorize(lambda x: x + amount)
    return np.apply_along_axis(inc_func, 1, area)


def decrease(area, amount):
    """
    Decreases values in an numpy array by amount.
    Args:
        area (np.array): area of work
        amount (int): amount by which we decrease
    Returns:
        np.array: decreased numpy array
    """

    dec_func = np.vectorize(lambda x: x - amount)
    return np.apply_along_axis(dec_func, 1, area)
