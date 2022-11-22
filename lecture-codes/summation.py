def summation(n, term):
    """
    The generic function to calculate the summation of the first n element determined by the term fuction

    >>> summation(5, cube)
    225
    """
    total, k = 0, 1
    while k <= n:
        total, k = total + term(k), k + 1
    return total

def identity(n):
    return n

def square(n):
    return n * n

def cube(n):
    return n ** 3

def sum_naturals(n):
    return summation(n, identity)
