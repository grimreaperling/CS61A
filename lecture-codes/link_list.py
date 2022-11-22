class Link:

    empty = ()

    def __init__(self, first, rest=empty):
        assert rest is Link.empty or isinstance(rest, Link)
        self.first = first 
        self.rest = rest
   
def add(s, v):
    """Add v to s, returning modified s."""

    assert s is not Link.empty
    if s.first > v:
        s.first, s.rest = v, List(s.first, s.rest)
    elif s.first < v and s.rest == Link.empty:
        s.rest = Link(v)
    elif s.first < v:
        add(s.rest, v)
    return s

        
