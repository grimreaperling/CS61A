class Link:
    """A linked list.

    >>> Link(1, Link(2, Link(3)))
    Link(1, Link(2, Link(3)))
    >>> s = Link(1, Link(Link(2, Link(3)), Link(4)))
    >>> s
    Link(1, Link(Link(2, Link(3)), Link(4)))
    >>> print(s)
    <1 <2 3> 4>
    """

    empty = ()

    def __init__(self, first, rest=empty):
        assert rest is Link.empty or isinstance(rest, Link)
        self.first = first
        self.rest = rest

    def __repr__(self):
        if self.rest:
            rest_repr = ', ' + repr(self.rest)
        else:
            rest_repr = ''
        return 'Link(' + repr(self.first) + rest_repr + ')'

    def __str__(self):
        string = '<'
        while self.rest is not Link.empty:
            string += str(self.first) + ' '
            self = self.rest
        return string + str(self.first) + '>'

def ordered(lnk, key=lambda x: x):
    #  curr = lnk
    #  while curr.rest != Link.empty:
    #      if (curr.rest.first < curr.first):
    #          return False
    #      curr = curr.rest
    #  return True
    if lnk == Link.empty or lnk.rest == Link.empty:
        return True
    elif key(lnk.rest.first) < key(lnk.first):
        return False
    else:
        return ordered(lnk.rest, key)


def merge(s, t):
    if s.rest == Link.empty:
        return t
    elif t.rest == Link.empty:
        return s
    elif s.first <= t.first:
        return Link(s.first, merge(s.rest, t))
    else:
        return Link(t.first, merge(s, t.rest))

def merge_in_place(s, t):
    if s.rest == Link.empty:
        return t
    elif t.rest == Link.empty:
        return s
    elif s.first <= t.first:
        s.rest = merge_in_place(s.rest, t)
        return s
    else:
        t.rest = merge_in_place(s, t.rest)
        return t
