"""Our first Python source file."""

from operator import floordiv, mod

def divide_exact(n, d):
    """Return the quotient and remainder of dividing N by D."""
    return floordiv(n, d), mod(n, d)

q, r  = divide_exact(2013, 10)