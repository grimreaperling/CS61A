from operator import mul

def sum_squares(x, y):
    """
    >>> sum_squares(1, 2) 
    5
    """
    return square(x) + square(y)

def square(x):
    """
    >>> square(3)
    9
    """
    return mul(x, x)


