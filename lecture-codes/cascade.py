from ucb import trace

@trace
def cascade(n):
    if n < 10:
        print(n)
    else:
        print(n)
        cascade(n // 10)
        print(n)

def cascade_simple(n):
    print(n)
    if n >= 10:
        cascade_simple(n // 10)
        print(n)

def inverse_cascade(n):
    grow(n)
    print(n)
    shrink(n)

def f_then_g(f, g, n):
    if n:
        f(n)
        g(n)

grow = lambda n: f_then_g(grow, print, n // 10)
shrink = lambda n:f_then_g(print, shrink, n // 10)
