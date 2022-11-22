def print_sums(n):
    """Arise from a tricky task"""
    print(n)
    def next_sum(k):
        return print_sums(n+k)      
    return next_sum

def curry2(f):
    """
    The most naive implementation of the curry function
    >>> from operator import mul
    >>> f = curry2(mul)
    >>> f(2)(3)
    6
    """
    def g(x):
        def h(y):
            return f(x, y)
        return h
    return g

def curry(f):
    """Implement the curry function use the lambda expression"""
    return lambda x: lambda y: f(x, y)

def delay(arg):
    print("delayed")
    def g():
        return arg
    return g

result = delay(delay)()(6)()
