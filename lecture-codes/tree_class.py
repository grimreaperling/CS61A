class Tree:
    def __init__(self, label, branches=[]):
        self.label = label 
        for branch in branches:
            assert isinstance(branch, Tree)
        self.branches = list(branches)

def prune(t, n):
    """Prune all the subtree whose label is n."""
    t.branches = [b for b in t.branches if b.label != n]
    for b in t.branches:
        prune(b, n)



        
