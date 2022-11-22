a = 1
def f(g):
    a = 2
    return lambda y: a + g(y)

def end(n, d):
    """
    Print the given digit in a reverse order
    >>> end(23546, 4)
    6
    4
    """
    "*** CODE ***"

def search(f):
    """
    >>> x = lambda x: x == 1
    >>> search(x)
    1
    """
    x = 0;
    while True:
        if f(x):
            return x
        x += 1

def search_shorter(f):
    """Same function to the search different implementation"""
    x = 0
    while not f(x):
        x += 1
    return x

def square(x):
    """Return the square of x"""
    return x*x

def inverse(f):
    """Retrun g(x) such that f(g(x)) -> x"""
    return lambda x: search(lambda y: f(y) == x)


result = f(lambda y: a + y)(a)


