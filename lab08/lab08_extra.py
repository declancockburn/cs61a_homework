""" Extra questions for Lab 08 """

from lab08 import *

# OOP
class Keyboard:
    """A Keyboard takes in an arbitrary amount of buttons, and has a
    dictionary of positions as keys, and values as Buttons.

    >>> b1 = Button(0, "H")
    >>> b2 = Button(1, "I")
    >>> k = Keyboard(b1, b2)
    >>> k.buttons[0].key
    'H'
    >>> k.press(1)
    'I'
    >>> k.press(2) #No button at this position
    ''
    >>> k.typing([0, 1])
    'HI'
    >>> k.typing([1, 0])
    'IH'
    >>> b1.times_pressed
    2
    >>> b2.times_pressed
    3
    """

    def __init__(self, *args):
        # self.buttons = [arg for arg in args]
        self.buttons = {}
        for arg in args:
            self.buttons[arg.pos] = arg
        "*** YOUR CODE HERE ***"

    def press(self, info):
        """Takes in a position of the button pressed, and
        returns that button's output"""
        if info in self.buttons.keys():
            self.buttons[info].times_pressed += 1
            return self.buttons[info].key
        else:
            return ''

    def typing(self, typing_input):
        """Takes in a list of positions of buttons pressed, and
        returns the total output"""
        output = []
        for i in typing_input:
            output.append(self.press(i))
        return ''.join(output)
        "*** YOUR CODE HERE ***"

class Button:
    def __init__(self, pos, key):
        self.pos = pos
        self.key = key
        self.times_pressed = 0


##

# Nonlocal
def make_advanced_counter_maker():
    """Makes a function that makes counters that understands the
    messages "count", "global-count", "reset", and "global-reset".
    See the examples below:

    >>> make_counter = make_advanced_counter_maker()
    >>> tom_counter = make_counter()
    >>> tom_counter('count')
    1
    >>> tom_counter('count')
    2
    >>> tom_counter('global-count')
    1
    >>> jon_counter = make_counter()
    >>> jon_counter('global-count')
    2
    >>> jon_counter('count')
    1
    >>> jon_counter('reset')
    >>> jon_counter('count')
    1
    >>> tom_counter('count')
    3
    >>> jon_counter('global-count')
    3
    >>> jon_counter('global-reset')
    >>> tom_counter('global-count')
    1
    """
    global_count = 0

    def wrapper():
        count = 0

        def counter(place):
            nonlocal global_count
            nonlocal count
            if place == "count":
                count += 1
                return count
            elif place == "global-count":
                global_count += 1
                return global_count
            elif place == "reset":
                count = 0
            elif place == "global-reset":
                global_count = 0
        return counter
    return wrapper

make_counter = make_advanced_counter_maker()
tom_counter = make_counter()
tom_counter('count')
tom_counter('count')
tom_counter('global-count')
jon_counter = make_counter()
jon_counter('global-count')


##
# Lists
def trade(first, second):
    """Exchange the smallest prefixes of first and second that have equal sum.

    >>> a = [1, 1, 3, 2, 1, 1, 4]
    >>> b = [4, 3, 2, 7]
    >>> trade(a, b) # Trades 1+1+3+2=7 for 4+3=7
    'Deal!'
    >>> a
    [4, 3, 1, 1, 4]
    >>> b
    [1, 1, 3, 2, 2, 7]
    >>> c = [3, 3, 2, 4, 1]
    >>> trade(b, c)
    'No deal!'
    >>> b
    [1, 1, 3, 2, 2, 7]
    >>> c
    [3, 3, 2, 4, 1]
    >>> trade(a, c)
    'Deal!'
    >>> a
    [3, 3, 2, 1, 4]
    >>> b
    [1, 1, 3, 2, 2, 7]
    >>> c
    [4, 3, 1, 4, 1]
    """
    m, n = 1, 1

    def helper():
        nonlocal m, n
        while m <= len(first) and n <= len(second):
            if sum(first[:m]) == sum(second[:n]):
                return True
            elif sum(first[:m]) < sum(second[:n]):
                m += 1
                return helper()
            elif sum(first[:m]) > sum(second[:n]):
                n += 1
                return helper()
        return False
    deal = helper()
    if deal: # change this line!
        first[:m], second[:n] = second[:n], first[:m]
        return 'Deal!'
    else:
        return 'No deal!'


##
# Generators

def permutations(seq):
    """Generates all permutations of the given sequence. Each permutation is a
    list of the elements in SEQ in a different order. The permutations may be
    yielded in any order.

    >>> perms = permutations([100])
    >>> type(perms)
    <class 'generator'>
    >>> next(perms)
    [100]
    >>> try:
    ...     next(perms)
    ... except StopIteration:
    ...     print('No more permutations!')
    No more permutations!
    >>> sorted(permutations([1, 2, 3])) # Returns a sorted list containing elements of the generator
    [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
    >>> sorted(permutations((10, 20, 30)))
    [[10, 20, 30], [10, 30, 20], [20, 10, 30], [20, 30, 10], [30, 10, 20], [30, 20, 10]]
    >>> sorted(permutations("ab"))
    [['a', 'b'], ['b', 'a']]
    """
    if len(seq) == 0:
        yield []
    else:
        for perm in permutations(seq[1:]):
            # print(perm)
            for i in range(len(perm)+1):
                yield perm[:i] + [seq[0]] + perm[i:]


sorted(permutations([1, 2, 3, 4]))



# lst = [1,2,3,4]
# value = 'hi'
# i = 2
#
# lst[:i] + [value] + lst[i:]
# [x for x in lst].insert(i, value)


##

# Recursive objects
def make_to_string(front, mid, back, empty_repr):
    """ Returns a function that turns linked lists to strings.

    >>> kevins_to_string = make_to_string("[", "|-]-->", "", "[]")
    >>> jerrys_to_string = make_to_string("(", " . ", ")", "()")
    >>> lst = Link(1, Link(2, Link(3, Link(4))))
    >>> kevins_to_string(lst)
    '[1|-]-->[2|-]-->[3|-]-->[4|-]-->[]'
    >>> kevins_to_string(Link.empty)
    '[]'
    >>> jerrys_to_string(lst)
    '(1 . (2 . (3 . (4 . ()))))'
    >>> jerrys_to_string(Link.empty)
    '()'
    """
    def helper(lst):
        if isinstance(lst, Link):
            if lst.rest is not Link.empty:
                rest = mid + helper(lst.rest)
            else:
                rest = mid + empty_repr
            return front + helper(lst.first) + str(rest) + back
        else:
            if lst is Link.empty:
                return empty_repr
            else:
                return str(lst)

    return helper

##
# kevins_to_string = make_to_string("[", "|-]-->", "", "[]")
# jerrys_to_string = make_to_string("(", " . ", ")", "()")
# lst = Link(1, Link(2, Link(3, Link(4))))
# lst = Link(7, Link(Link(8, Link(9))))
# # lst.__str__()
# kevins_to_string(lst)
# jerrys_to_string(lst)
# kevins_to_string(Link.empty)


#
# type(lst.first)
#
# tst = Link(7, Link(Link(8, Link(9))))
# tst.first
# tst.rest.first


##


def tree_map(fn, t):
    """Maps the function fn over the entries of t and returns the
    result in a new tree.

    >>> numbers = Tree(1,
    ...                [Tree(2,
    ...                      [Tree(3),
    ...                       Tree(4)]),
    ...                 Tree(5,
    ...                      [Tree(6,
    ...                            [Tree(7)]),
    ...                       Tree(8)])])
    >>> print(tree_map(lambda x: 2**x, numbers))
    2
      4
        8
        16
      32
        64
          128
        256
    >>> print(numbers)
    1
      2
        3
        4
      5
        6
          7
        8
    """
    def print_tree(tr, indent=0):
        tree_str = '  ' * indent + str(fn(tr.label)) + "\n"
        for b in tr.branches:
            tree_str += print_tree(b, indent + 1)
        return tree_str
    return print_tree(t).rstrip()



##

def long_paths(tree, n):
    """Return a list of all paths in tree with length at least n.

    >>> t = Tree(3, [Tree(4), Tree(4), Tree(5)])
    >>> left = Tree(1, [Tree(2), t])
    >>> mid = Tree(6, [Tree(7, [Tree(8)]), Tree(9)])
    >>> right = Tree(11, [Tree(12, [Tree(13, [Tree(14)])])])
    >>> whole = Tree(0, [left, Tree(13), mid, right])
    >>> for path in long_paths(whole, 2):
    ...     print(path)
    ...
    <0 1 2>
    <0 1 3 4>
    <0 1 3 4>
    <0 1 3 5>
    <0 6 7 8>
    <0 6 9>
    <0 11 12 13 14>
    >>> for path in long_paths(whole, 3):
    ...     print(path)
    ...
    <0 1 3 4>
    <0 1 3 4>
    <0 1 3 5>
    <0 6 7 8>
    <0 11 12 13 14>
    >>> long_paths(whole, 4)
    [Link(0, Link(11, Link(12, Link(13, Link(14)))))]
    """

    def make_line(t, fn, i):
        # if t.is_leaf():
        #     # print(fn(t.label).__repr__())
        #     if i >= n:
        #         output_lst.append(fn(t.label))
        # else:
        if t.is_leaf() and i >= n:
            output_lst.append(Link(t.label))
        else:
            for b in t.branches:
                if b.is_leaf():
                    fni = lambda x, y: fn(x, Link(y))
                    if i >= n:
                        output_lst.append(fni(t.label, b.label))
                else:
                    fni = lambda x, y: fn(t.label, Link(x, y))
                    make_line(b, fni, i + 1)

    fun = lambda x, y: Link(x, y)
    output_lst = []
    make_line(tree, fun, 1)
    return output_lst


# t = Tree(3, [Tree(4), Tree(4), Tree(5)])
# left = Tree(1, [Tree(2), t])
# mid = Tree(6, [Tree(7, [Tree(8)]), Tree(9)])
# right = Tree(11, [Tree(12, [Tree(13, [Tree(14)])])])
# whole = Tree(0, [left, Tree(13), mid, right])
#
# for path in long_paths(whole, 4):
#     print(path)
#
# long_paths(whole, 4)
# long_paths(whole, 3)
#
# len(long_paths(whole, 4))

##
# Orders of Growth
def zap(n):
    i, count = 1, 0
    while i <= n:
        while i <= 5 * n:
            count += i
            print(i / 6)
            i *= 3
    return count

def boom(n):
    sum = 0
    a, b = 1, 1
    while a <= n*n:
        while b <= n*n:
            sum += (a*b)
            b += 1
        b = 0
        a += 1
    return sum

boom(5)

## Tree class
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