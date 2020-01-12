# -*- coding: utf-8 -*-
"""
Created by dcockbur on 10/09/2018	
"""
#%%


##
def split(n):
    return n // 10, n % 10

def sum_digits(n):
    """return sum of digits of positive integer n"""
    if n < 10:
        return n
    else:
        all_but_last, last = split(n)
        return sum_digits(all_but_last) + last

sum_digits(1231020001213992)

##
def fact(n):
    if n == 0:
        return 1
    else:
        return n * fact(n-1)

##
x = 4
y = x*7
a = x * x * y

x=2
print(a)

##

def make_adder(n):
    return lambda k: n + k

##

(lambda f, x: f(x))(lambda y: y + 1, 10)

##

def split_n(n):
    if n < 100:
        return n % 10
    else:
        return n // 100, n % 10

split_n(12345)


##
def sum_every_other_digit(n):
    """
    >>> sum_every_other_digit(7)
    7
    >>> sum_every_other_digit(30)
    0
    >>> sum_every_other_digit(228)
    10
    >>> sum_every_other_digit(123456)
    12
    >>> sum_every_other_digit(1234567) # 1 + 3 + 5 + 7
    16
    """
    print(n)
    if n < 10:
        return n
    elif n < 100:
        return n % 10
    else:
        rest, last = split_n(n)
        return sum_every_other_digit(rest) + last

sum_every_other_digit(78123456)

##

def cascade(n):
    if n<10:
        print(n)
    else:
        print(n)
        cascade(n//10)
        print(n)

cascade(123)

##

def inverse_cascade(n):
    grow(n)
    print(n)
    shrink(n)

def f_then_g(f, g, n):
    if n:
        f(n)
        g(n)

grow = lambda n: f_then_g(grow, print, n//10)
shrink = lambda n: f_then_g(print, shrink, n//10)

inverse_cascade(12345)

##
# Fibonacci

def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-2) + fib(n-1)

fib(5)

##
# Count recursions

def count_partition(n, m):
    if n == 0:
        return 1
    elif n < 0:
        return 0
    elif m == 0:
        return 0
    else:
        with_m = count_partition(n-m, m)
        without_m = count_partition(n, m-1)
        return with_m + without_m

count_partition(24, 4)

##

def is_prime(n):
    """
    >>> is_prime(7)
    True
    >>> is_prime(10)
    False
    >>> is_prime(1)
    False
    """
    def prime_helper(idx):
        if idx == n:
            return True
        elif n % idx == 0 or n == 1:
            return False
        else:
            return prime_helper(idx+1)
    return prime_helper(2)

is_prime(103)

##

def make_func_repeater(f, x):
    """
    >>> incr_1 = make_func_repeater(lambda x: x+1, 1)
    >>> incr_1(2) # same as f(f(x))
    3
    >>> incr_1(5)
    6
    """
    def repeat(i):
        if i == 0:
            return x
        else:
            return f(repeat(i-1))
    return repeat


incr_4 = make_func_repeater(lambda x: x + 1, 7)
# incr_4(4) = 8
incr_4(4)

##

def count_stair_ways(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        return count_stair_ways(n-1) + count_stair_ways(n-2)

count_stair_ways(4)

## Recursion problems continued

def count_k(n, k):
    """
    >>> count_k(3, 3) # 3, 2 + 1, 1 + 2, 1 + 1 + 1
    4
    >>> count_k(4, 4)
    8
    >>> count_k(10, 3)
    274
    >>> count_k(300, 1) # Only one step at a time
    1
    """
    if n == 0:
        return 1
    elif n <0:
        return 0
    else:
        tot = 0
        i = 1
        while i <=k:
            tot += count_k(n-i, k)
            i+=1
        return tot

count_k(10,3)

## Pascal's triangle

def pascal(row, column):
    """draw tree and work out base cases:
    base case 1:
    if r < c return 0
    if r == c return 1
    if  c < 0 return 0
    """
    if row < column:
        return 0
    elif row == column:
        return 1
    elif column < 0:
        return 0
    else:
        return pascal(row-1, column) + pascal(row-1, column-1)


pascal(25, 12)

## recursive function

x = [1,2,3,4,5,6]

def addition(array):
    if len(array) == 0:
        return 0
    else:
        return array[0] + addition(array[1:])

print(addition(x))


## Data abstraction: selectors and constructors
# Creating a barrier between the data and the data type
def numer(x):
      return x('n')

def denom(x):
      return x('d')

def rational(n, d):
      def select(name):
            if name == 'n':
                  return n
            if name == 'd':
                  return d
      return select

x = rational(3,8)
numer(x)


## CS 61a exam prep week 9/10
# Recursion fill-in, tree recursion fill0n

## Print Numbers
def print_numbers(n, k):
    """Print all numbers that (A) can be formed from the digits
    of `n` in reverse order and (B) are multiples of `k`.
    This is essentially Fall 2015 Midterm 2 #3c written to not
    depend on knowledge of lists.
    Args:
    n (int): The number that results must use digits from.
    k (int): The number that results must be multiples of.
    >>> print_numbers(97531, 5)
    135
    15
    35
    >>> print_numbers(97531, 7)
    1379
    357
    35
    >>> print_numbers(97531, 2)
    """
    def inner(n, s):
        if n == 0:
            if s % k == 0 and s > k:
                print("RESULT:    {}".format(s))
        else:
            # print("({}, {})".format(n,s))
            s2 = n % 10 + s * 10
            n = n // 10
            # print("({}, {}), ({}, {})".format(n,s2,n,s))
            inner(n, s2)
            inner(n, s)
    inner(n, 0)

# print_numbers(97531, 5)

print_numbers(97531, 2)


## Sixty Ones

def sixty_ones(n):
    """Return the number of times that a 1 directly follows a 6
    in the digits of `n`.
    This is essentially Fall 2014 Midterm 2 #3a written to not
    depend on knowledge of lists.
    Args:
    n (int): The number whose digits are to be examined.
    Returns:
    int: The number of occurrences.
    >>> sixty_ones(461601)
    1
    >>> sixty_ones(161461601)
    2
    """
    if n < 61:
        return 0
    elif n % 100 == 61:
        return sixty_ones(n//100) + 1
    else:
        return sixty_ones(n//10)


#SUCCESS! I got this one on my own :)
sixty_ones(461601)


## No Elevens
def no_elevens(n):
    """Return the number of `n`-digit numbers whose digits
    consist of 1's and 6's and do not contain a `1` and
    then another `1` consecutively.
    This is essentially Fall 2014 Midterm 2 #3b rewritten to
    not depend on knowledge of lists.
    Args:
    n (int): The length of the numbers.
    Returns:
    int: The number of numbers.
    >>> no_elevens(2) # 66, 61, 16
    3
    >>> no_elevens(3) # 666, 661, 616, 166, 161
    5
    >>> no_elevens(4) # 6666, 6661, 6616, 6166, 1666, 1661, 1616, 6161
    8
    """
    if n == 0:
        return 1
    elif n == 1:
        return 2
    else:
        return no_elevens(n-1) + no_elevens(n-2)

no_elevens(6)

##
def no_elevens2(n):
    """Return the number of `n`-digit numbers whose digits
    consist of 1's and 6's and do not contain a `1` and
    then another `1` consecutively.
    This is essentially Fall 2014 Midterm 2 #3b rewritten to
    not depend on knowledge of lists.
    Args:
    n (int): The length of the numbers.
    Returns:
    int: The number of numbers.
    >>> no_elevens2(2) # 66, 61, 16
    3
    >>> no_elevens2(3) # 666, 661, 616, 166, 161
    5
    >>> no_elevens2(4) # 6666, 6661, 6616, 6166, 1666, 1661, 1616, 6161
    8
    """
    if n == 0:
        return 0
    elif n == 1:
        return 2
    else:
        return no_elevens2(n - 1) + n - 1


no_elevens2(6)

## Guerilla section 3:  Sequences, Data Abstraction, and Trees

# Question 0


lst = [1, 2, 3, 4, 5]
lst[1:3] # [2, 3]
lst[0:len(lst)] # [1, 2, 3, 4, 5]
lst[-4:] # [2,3,4,5]
lst[:3] # [1,2,3]
lst[3:] # [4, 5]
lst[:] # [1, 2, 3, 4, 5]

# easy
lst[1:4:2] # [2,4]
lst[0:4:3] # [1,4]
lst[:4:2] # [1,3]
lst[1::2] # [2,4]
lst[::2] # [1,3,5]
lst[::-1] # [5,4,3,2,1]
lst2 = [6, 1, 0, 7]
lst + lst2 # [1, 2, 3, 4, 5, 6, 1, 0, 7]
lst + 100 # [1, 2, 3, 4, 5, 100] # GOT THIS ONE WRONG, + concats iterables, can't add an integer to iterable.
lst3 = [[1], [2], [3]]
lst + lst3 # [1, 2, 3, 4, 5, [1], [2], [3]]

## Question 2

"""Write combine_skipper, which takes in a function f and list lst and outputs a list. When
this function takes in a list lst, it looks at the list in chunks of four and applies f to the first two
elements in every set of four elements and replaces the first element with the output of the
function f applied to the two elements as the first value and the index of the second item of the
original two elements as the second value of the new two elements. f takes in a list and outputs
a value. [Assume the length of lst will always be divisible by four]"""

def combine_skipper(f, lst):
    n = 0
    while n < len(lst) // 4:
        i = n*4
        lst[i] = f(lst[i:i+2])
        lst[i+1] = i + 1
        n+=1
    return lst

lst = [4, 7, 3, 2, 1, 8, 5, 6]
f = lambda l: sum(l)
lst = combine_skipper(f, lst)
lst

lst2 = [4, 3, 2, 1]
lst2 = combine_skipper(f, lst2)
lst2
# easy
"""
>>> lst = [4, 7, 3, 2, 1, 8, 5, 6]
>>> f = lambda l: sum(l)
>>> lst = combine_skipper(f, lst)
>>> lst
[11, 1, 3, 2, 9, 5, 5, 6]
>>> lst2 = [4, 3, 2, 1]
>>> lst2 = combine_skipper(f, lst2)
>>> lst2
[7, 1, 2, 1]
"""

## Will it work? no
# I was wrong

a = 1
b = 2
dt = {a:1,b:2}

print(dt)

## Will it work? yes
# No I was wrong

a = [1]
b = [2]
dt = {a:1,b:2}

print(dt)

##
a = [1, [2, 3], 4]
c = a[1]
c
a.append(c)
a
c[0] = 0
c
a
a.extend(c)
c[1] = 9
a
##
lst = [5, 6, 7]
risk = [5, 6, 7]
lst, risk = risk, lst
lst is risk

# True

##
mist = risk
risk = risk[0:4]
mist.insert(-1, 99)
risk[-1]

# 99

##
# Hint: Try drawing the result of [y + 1 for y in mist] first.
risk = [x for x in [y + 1 for y in mist] if x % 10 != 0]
risk

#6 7 100 8
#6 7 8

##
er = [1, 2]
er.extend(risk.pop())
er
#1,2,6,7

##
a = [1]
b = [1]
a is b

## express the following as def statements:

#i. pow = lambda x, y: x**y

def pow(x,y):
    return x**y


# ii. foo = lambda x: lambda y: lambda z: x + y * z

def foo(x, y, z):
    return x + y * z

# iii. compose = lambda f, g: lambda x: f(g(x))

def compose(f,g,x):
    return f(g(x))


## Week 7 lecture 19: Growth

# Fib, efficiency.

def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-2) + fib(n-1)


def count(f):
    def counted(n):
        counted.call_count += 1
        return f(n)
    counted.call_count = 0
    return counted

fib = count(fib)

fib(5)
fib(6)
fib.call_count

## Memoization:
# Note: you can only really memoize pure functions and expect their behaviour to stay the same.
# Todo: what's a pure function?


def memo(f):
    cache = {}

    def memoized(n):
        if n not in cache:
            cache[n] = f(n)
        return cache[n]
    return memoized

fib(30)

fib.call_count

fib = memo(fib)
fib = count(fib)

fib(70)
fib.call_count

fib.cache
fib

## Space/memory
#Note: Values take up space, as do open frames. So lets count the max open frames at any one time:


def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-2) + fib(n-1)


def count_frames(f):
    def counted(n):
        counted.open_count += 1
        if counted.open_count > counted.max_count:
            counted.max_count = counted.open_count
        result = f(n)
        counted.open_count -= 1
        return result
    counted.open_count = 0
    counted.max_count = 0
    return counted

fib(5)
fib = count_frames(fib)
fib(20)
fib.max_count

## Time:


def count(f):
    def counted(*args):
        counted.call_count += 1
        return f(*args)
    counted.call_count = 0
    return counted


def divides(k, n):
    return n % k == 0


def factors(n):
    total = 0
    for k in range(1, n+1):
        if divides(k, n):
            total += 1
    return total


divides = count(divides)

factors(6)
factors(24)

divides.call_count

from math import sqrt


def factors_fast(n):
    total = 0
    sqrt_n = sqrt(n)
    k = 1
    while k < sqrt_n:
        if divides(k, n):
            total += 2
        k += 1

    if k*k == n:
        total += 1
    return total

factors_fast(500)
factors(500)
divides = count(divides)
divides.call_count


## Exponention

import time



def exp(n):
    b = 2
    if n == 0:
        return 1
    else:
        return b * exp(n-1)


print(exp(3))


def square(x):
    return x*x


def fast_exp(n):
    b = 2
    if n == 0:
        return 1
    elif n % 2 == 0:
        return square(fast_exp(n//2))
    else:
        return b * fast_exp(n-1)


# t1 = time.time()
# exp(100)
# t2 = time.time()
# fast_exp(100)
# t3 = time.time()
#
# print(1000000*(t2-t1))
# print(1000000*(t3-t2))

from timeit import repeat
from numpy import median, sum

g = globals()
n=50000
# name = 'exp'
name = 'fast_exp'
f1 = lambda x: 'exp' + '(' + str(x) + ')'
f2 = lambda x: 'fast_exp' + '(' + str(x) + ')'
time1 = lambda x: repeat(f1(x), globals=g, number=1, repeat=n)
time2 = lambda x: repeat(f2(x), globals=g, number=1, repeat=n)

print(sum(time1(199)))
print(sum(time2(199)))



## Sets

s1 = {1,3,4}
s2 = {2,3,5}

#union, intersection, adjoin

##

def empty(s):
    return s is Link.empty

def contains(s, v):
    """Return True if set s contains value v as an element

    >>> s = Link(1, Link(3, Link(2)))
    >>> contains(s, 2)
    True
    >>>

    """


##

class Bear:
    """A Bear."""
    def __init__(self):
        self.__repr__ = lambda: 'oski'
        self.__str__ = lambda: 'this bear'

    def __repr__(self):
        return 'Bear()'

    def __str__(self):
        return 'a bear'

oski = Bear()

print(oski)
print(str(oski))
print(repr(oski))
print(oski.__str__())
print(oski.__repr__())

##

s = [2, 3]
t = [5, 6]

s.append(t)
t = 0

s.extend(t)
t[1] = 0

s
t
a
b

a = s + [t]
b = a[1:]
a[1] = 9
b[1][1] = 0

##

t = [1, 2, 3]
t
t[1:3] = [t]
t
t.extend(t)
t

# t = [1, 2, 3]
# t = [1, [1, 2, 3]]
# t = [1, [1, 2, 3], 1, [1, 2, 3]]
##
t = [[1, 2], [3, 4]]
t[0].append(t[1:2])
t
# t = [[1, 2, [3, 4]], [3, 4]]

## Sierpinski's Triangle


