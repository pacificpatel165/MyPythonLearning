"""
Problem
You have a nested sequence that you want to flatten into a single list of values.
"""

# Solution
# This is easily solved by writing a recursive generator function involving a yield from
# statement. For example:

from collections import Iterable


def flatten(items, ignore_types=(str, bytes)):
    for x in items:
        if isinstance(x, Iterable) and not isinstance(x, ignore_types):
            yield from flatten(x)
        else:
            yield x


items = [1, 2, [3, 4, [5, 6], 7], 8]

# Produces 1 2 3 4 5 6 7 8
for x in flatten(items):
    print(x)

items = ['Dave', 'Paula', ['Thomas', 'Lewis']]
for x in flatten(items):
    print(x)


# The yield from statement is a nice shortcut to use if you ever want to write generators
# that call other generators as subroutines. If you don’t use it, you need to write code that
# uses an extra for loop. For example:

def flatten(items, ignore_types=(str, bytes)):
    for x in items:
        if isinstance(x, Iterable) and not isinstance(x, ignore_types):
            for i in flatten(x):
                yield i
        else:
            yield x
