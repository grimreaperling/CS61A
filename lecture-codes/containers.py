from operator import add, mul
def reduced(fn, lst, start):
    for element in lst:
        start = fn(element, start)
    return start

def sum(lst, start=0):
    return reduced(add, lst, start)

def product(lst, start=1):
    return reduced(mul, lst, start)
