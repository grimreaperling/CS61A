def count_partition(n, m):
    if n == 0:
        return 1
    elif n < 0:
        return 0
    elif m == 0:
        return 0
    else:
        with_m = count_partition(n - m, m)
        without_m = count_partition(n, m - 1)
        return without_m + with_m
