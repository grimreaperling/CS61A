def evens(start, end):
    even = start + (start % 2)
    while even < end:
        yield even
        even = even + 2

def a_then_b(a, b):
    yield from a
    yield from b

def count_down(k):
    if k > 0:
        yield k
        yield from count_down(k - 1)

def prefixes(s):
    if s:
        yield from prefixes(s[:-1])
        yield s

def substrings(s):
    if s:
        yield from prefixes(s)
        yield from substrings(s[1:])

def count_partitions(n, m):
    """Count partitions.

    >>> count_partitions(6, 4)
    9
    """
    if n < 0 or m == 0:
        return 0
    else:
        exact_match = 0
        if n == m:
            exact_match = 1
        with_m = count_partitions(n - m, m)
        without_m = count_partitions(n, m - 1)
        return exact_match + without_m + with_m

def partitions(n, m):
    """Yield the partitions."""
    if n > 0 and m > 0:
        if n == m:
            yield str(m)
        for p in partitions(n - m, m):
            yield p + '+' + str(m)
        yield from partitions(n, m - 1)


        
