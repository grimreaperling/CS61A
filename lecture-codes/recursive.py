def split(n):
    """Split the input positive digits""" 
    return n // 10, n % 10

def sum_digits(n):
    """Return the sum of the digits of positive integer n"""
    if n < 10:
        return n
    else:
        all_but_last, last = split(n)
        return sum_digits(all_but_last) + last

def sum_digits_iter(n):
    """The iterative version"""
    digit_sum = 0
    while n > 0:
        n, last = split(n)
        digit_sum = digit_sum + last
    return digit_sum

def fact(n):
    """
    A recursive way to define the factorial function
    >>> fact(3)
    6
    """
    if n == 0:
        return 1
    else:
        return fact(n - 1) * n

def fact_iteration(n):
    """An iterative implementation for the factorial fucntion"""
    result, k = 1, 1
    while k <= n:
        result, k = result * k, k + 1
    return result

def luhn_sum(n):
    if n < 10:
        return n
    else:
        all_but_last, last = split(n)
        return luhn_sum_double(all_but_last) + last

def luhn_sum_double(n):
    all_but_last, last = split(n)
    luhn_digit = sum_digits(2 * last)
    if n < 10:
        return luhn_digit
    else:
        return luhn_sum(all_but_last) + luhn_digit

def fib(n):
    """Count the nth number in the fib sequence"""
    if n == 1:
        return 0
    if n == 2:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


