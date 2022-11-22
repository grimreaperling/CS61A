def search(query, ranking=lambda r: -r.stars):
    results = [r for r in Restaurant.all if query in r.name]
    return sorted(results, key=ranking)

def reviewed_both(r, o):
     # return len([x for x in r.reviewers if x in o.reviewers])
     return fast_overlap(r.reviewers, o.reviewers)

def fast_overlap(s, t):
    """Return the overlap between the sorted s and sorted t."""
    i, j, count = 0, 0, 0

    while i < len(s) and j < len(t):
        if s[i] = t[j]:
            count, i, j = count + 1, i + 1, j + 1
        elif s[i] > t[j]:
            j++
        else:
            i++
    return count
            

class Restaurant:
    all = []
    def __init__(self, name, star, reviewers):
        self.name, self.star = name, star
        self.reviewers = reviewers
        Restaurant.all.append(self)

    def similar(self, k, similarity=reviewed_both):
        """Return the k most similar restaurants to self"""
       others = list(Restaurant.all)
       others.remove(self)
       return sorted(others, key=lambda r: -similarity(r, self))[:k]

    def __repr__(self):
        return '<' + self.name + '<'
