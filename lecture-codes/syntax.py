from string import punctuation

contractions = ["n't", "'s", "'re", "'ve"]

def tree(label, branches=[]):
    if not branches:
        return [label];
    else:
        return ['(', label] + sum(branches, start=[]) + [')'] 

def label(tree):
    if len(tree) == 1:
        return tree[0]
    else:
        assert tree[0] == '(', tree
        return tree[1]

def branches(t):
    if t[0] != '(':
        return []
    opened = 1
    current_branch = []
    all_branches = []
    for token in t[2:]:
        current_branch.append(token)
        if token == '(':
            opened = opened + 1
        elif token == ')':
            opened = opened - 1
        if opened == 1:
            all_branches.append(current_branch)
            current_branch = []
    assert opened == 0
    return all_branches

def is_leaf(t):
    return not branches(t)

def leaves(t):
    if is_leaf(t):
        return [label(t)]
    else:
        return sum([leaves(b) for b in branches(t)], [])

example = tree('ROOT', 
               [tree('FRAG',
                     [tree('NP', 
                           [tree('DT', [tree('a')]),
                            tree('JJ', [tree('little')]),
                            tree('NN', [tree('bug')])]),
                      tree('.', [tree('.')])])])

def words(t):
    """Return the words of a tree as a string

    >>> words(example)
    'a little bug.'
    """
    s = ''
    for w in leaves(t):
        no_space = (w in punctuation and w != '$') or w in contractions
        if not s or no_space:
            s = s + w
        else:
            s = s + ' ' + w
    return s

def replace(t, s, w):
    """Return the tree like t with all nodes labeled s replaceed by word w

    >>> words(replace(example, "JJ", "huge"))
    'a huge bug.'
    """
    if label(t) == s:
        return tree(s, [tree(w)])
    else:
        return tree(label(t), [replace(b, s, w) for b in branches(t)])
