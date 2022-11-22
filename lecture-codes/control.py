def _if(c, t, f):
    if c:
        return t
    else:
        return f

from math import sqrt

def real_sqrt(x):
    _if(x > 0, sqrt(x), 0)

from math import sqrt

def has_big_sqrt(x):
    return x > 0 and sqrt(x) > 10

def reasonable(x):
    return x == 0 or 1 / x != 0 


