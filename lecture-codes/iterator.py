def double(x):
    print("**", x, "=>", 2 * x, "**")
    return 2 * x

def palindrome(s):
    """Return whether the s is the same backward and forward.

    >>> palindrome([3, 1, 4, 1, 5])
    False
    >>> palindrome([3, 1, 4, 1, 3])
    True
    """
    return all([a == b for a, b in zip(s, reversed(s))])

