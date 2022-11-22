def tree(label, branches=[]):
    for branch in branches:
        assert is_tree(branch)
    return [label] + list(branches)

def label(tree):
    return tree[0]

def branches(tree):
    return tree[1:]

def is_tree(tree):
    if type(tree) != list or len(tree) < 1:
        return False
    for branch in branches(tree):
        if not is_tree(branch):
            return False
    return True

def is_leaf(tree):
    return not branches(tree)

def fib_tree(n):
    if n <= 1:
        return tree(n)
    else:
        left, right = fib_tree(n - 2), fib_tree(n - 1)
        return tree(label(left) + label(right), [left, right])

def count_leaves(tree):
    """Return the leaves of the tree"""
    if is_leaf(t):
        return tree
    else:
        return sum([count_leaves(b) for b in branches(tree)])

def leaves(tree):
    """
    Return a list containing the leaf labels of the tree

    >>> leaves(fib_tree(5))
    [1, 0, 1, 0, 1, 1, 0, 1]
    """
    if is_leaf(tree):
        return [label(tree)]
    else:
        return sum([leaves(b) for b in branches(tree)], [])

def increment_leaves(tree):
    """Retrun a tree like t but with leaf labels incremented."""
    if is_leaf(tree):
        return tree(label(tree) + 1)
    else:
        return tree(label(tree), [increment_leaves(b) for b in branches(tree)])

def increment(tree):
    """Return a tree like t but with all labels incremented."""
    return tree(label(tree) + 1, [incremented(b) for b in branches(tree)])

def print_tree(t, indent=0):
    print(" " * indent + str(label(t)))
    for b in branches(t):
        print_tree(b, indent + 1)

def fact(n):
    if  n == 0:
        return 0
    else:
        return n * fact(n - 1)

def fact_times(n, k):
    """Return k * n * (n - 1) * ... * 1"""
    if n == 0:
       return k
    else:
       return fact_times(n - 1, k * n) 

