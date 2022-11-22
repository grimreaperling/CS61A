def make_adder(n):
    """
    RETUEN a function that take one number as a argument m then return m + n
    >>> add_three = make_adder(3)
    >>> add_three(4)
    7
    """
    def adder(k):
        return k + n
    return adder

