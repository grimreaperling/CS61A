def fib(n):
    """Compute the nth fibonacci number."""
    pred, curr = 1, 0
    k = 1
    while k < n:
        pred, curr = curr, pred + curr
        k = k + 1
    return curr
