# Slice assignment
def slice_assign():
    """
    Some examples to show the slice assignement, how it work related to the concept of the list mutation.

    >>> s = [2, 3]
    >>> t = [5, 6]
    >>> s[0:0] = t
    >>> s[3:] = t
    >>> t[1] = 0
    >>> s
    [5, 6, 2, 5, 6]
    >>> t
    [5, 0]
    """

def mystery():
    """
    This example include some tricky thing like list in list in list.

    >>> t = [1, 2, 3]
    >>> t[1:3] = [t]
    >>> t.extend(t)
    >>> t
    [1, [...], 1, [...]]
    >>> t = [[1, 2], [3, 4]]
    >>> t[0].append(t[1:2])
    >>> t
    [[1, 2, [[3, 4]]], [3, 4]]
    """
