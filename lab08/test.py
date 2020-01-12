# -*- coding: utf-8 -*-
""" Created by dcockbur (Declan Cockburn) on 5/21/2019 """


##

class Tree:
    """
    >>> t = Tree(3, [Tree(2, [Tree(5)]), Tree(4)])
    >>> t.label
    3
    >>> t.branches[0].label
    2
    >>> t.branches[1].is_leaf()
    True
    """
    def __init__(self, label, branches=[]):
        for b in branches:
            assert isinstance(b, Tree)
        self.label = label
        self.branches = list(branches)

    def is_leaf(self):
        return not self.branches

    def map(self, fn):
        """
        Apply a function `fn` to each node in the tree and mutate the tree.

        >>> t1 = Tree(1)
        >>> t1.map(lambda x: x + 2)
        >>> t1.map(lambda x : x * 4)
        >>> t1.label
        12
        >>> t2 = Tree(3, [Tree(2, [Tree(5)]), Tree(4)])
        >>> t2.map(lambda x: x * x)
        >>> t2
        Tree(9, [Tree(4, [Tree(25)]), Tree(16)])
        """
        self.label = fn(self.label)
        for b in self.branches:
            b.map(fn)

    def __contains__(self, e):
        """
        Determine whether an element exists in the tree.

        >>> t1 = Tree(1)
        >>> 1 in t1
        True
        >>> 8 in t1
        False
        >>> t2 = Tree(3, [Tree(2, [Tree(5)]), Tree(4)])
        >>> 6 in t2
        False
        >>> 5 in t2
        True
        """
        if self.label == e:
            return True
        for b in self.branches:
            if e in b:
                return True
        return False

    def __repr__(self):
        if self.branches:
            branch_str = ', ' + repr(self.branches)
        else:
            branch_str = ''
        return 'Tree({0}{1})'.format(self.label, branch_str)

    def __str__(self):
        def print_tree(t, indent=0):
            tree_str = '  ' * indent + str(t.label) + "\n"
            for b in t.branches:
                tree_str += print_tree(b, indent + 1)
            return tree_str
        return print_tree(self).rstrip()
##

t = Tree(3, [Tree(4), Tree(4, [Tree(8)]), Tree(5)])

lst = []
def make_line(t):

    nonlocal lst
    if t.is_leaf():
        return t
    else:
        for b in t.branches:
            lst.append(Tree(t.label, [make_line(b)]))


make_line(t)


##

def make_line(t, lsofar):
    if t.is_leaf():
        print(lsofar(t.label))
    else:
        for b in t.branches:
            fny = lambda y: lsofar(t.label, [y])
            make_line(b, fny(b))

tree = Tree(3, [Tree(4), Tree(4, [Tree(8)]), Tree(5)])
fn = lambda x: Tree(x)
make_line(tree, fn(tree.label))


##
fn = lambda x, y: Tree(x, [y])

a = fn(1, Tree(2))
a

##

fun = lambda x: Tree(x)

output_lst = []
n = 3

def make_line(t, fn, i):
    if t.is_leaf():
        print(fn(t.label).__repr__())
        if i >= n:
            output_lst.append(fn(t.label))
    else:
        fni = lambda y: Tree(t.label, [fn(y)])
        for b in t.branches:
            make_line(b, fni, i+1)

tree = Tree(1, [Tree(2), Tree(3, [Tree(4)]), Tree(5)])

# tree.is_leaf()
# tree.branches
make_line(tree, fun, 1)

output_lst


output_lst[1].branches[0].branches[0]


fun2 = lambda x: Tree(3, [fun(x)])
fun2

lst = []
lst.append(fun2(5))
lst