def count(s, value):
    """
    Count the number of times that value occurs in the sequence s
    >>> count([1, 2, 1, 2, 1], 1)
    3
    """
    total = 0
    for element in s:
        if element == value:
            total = total + 1
    return total

def count_same(pairs):
    """Input a list of pairs with two element, return the number of the pairs in 
    the list that have two identical element.
    >>> count_same([[1,2],[2,2]])
    1
    """
    total = 0
    for x, y in pairs:
        if x == y:
            total = total + 1
    return total 
    
def sum_below(n):
    """Count the total value evaluated by 1 + 2 + ... + n - 1(n is exclusive)
    >>> sum_below(3)
    3
    """
    total = 0
    for i in range(n):
        total = total + i
    return total

def cheer():
    for _ in range(3):
        print("Go Bears!")

def divisors(n):
    """Return all the divisors of the input n
    >>> divisors(5)
    [1]
    >>> divisors(6)
    [1, 2, 3]
    """
    return [1] + [x for x in range(2, n) if n % x == 0]
