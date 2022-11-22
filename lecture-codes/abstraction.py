from math import gcd

#def rational(m, n):
#    """A constructor for the rational"""
#    g = gcd(m, n)
#    return [m // g, n // g]
#
#def numer(lst):
#    return lst[0]
#
#def denom(lst):
#    return lst[1]

def mul_rational(x, y):
    return rational(numer(x) * numer(y), denom(x) * denom(y))

def add_rational(x, y):
    nx, dx = numer(x), denom(x)
    ny, dy = numer(y), denom(y)
    return rational(nx * dy + ny * dx, dx * dy)

def print_rational(x):
    print(numer(x), '/', denom(x))

def rational_are_equal(x, y):
    return numer(x) * denom(y) == numer(y) * denom(x)

#Constructor and the selector
def rational(n, d):
    """A constructor of the rational number use the high order function
    >>> x = rational(2, 3)
    >>> x('n')
    2
    >>> x('d')
    3
    """
    def select(name):
        if name == 'n':
            return n
        if name == 'd':
            return d
    return select

def numer(x):
    return x('n')

def denom(x):
    return x('d')
