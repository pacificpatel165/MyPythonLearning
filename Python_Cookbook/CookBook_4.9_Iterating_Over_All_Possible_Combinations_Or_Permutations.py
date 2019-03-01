"""
Problem
You want to iterate over all of the possible combinations or permutations of a collection
of items.
"""

# Solution
# The itertools module provides three functions for this task. The first of these—iter
# tools.permutations()—takes a collection of items and produces a sequence of tuples
# that rearranges all of the items into all possible permutations (i.e., it shuffles them into
# all possible configurations). For example:

from itertools import permutations

items = ['a', 'b', 'c']
for p in permutations(items):
    print(p)

# If you want all permutations of a smaller length, you can give an optional length argument.
# For example:

for p in permutations(items, 2):
    print(p)

# Use itertools.combinations() to produce a sequence of combinations of items taken
# from the input. For combinations(), the actual order of the elements is not considered. That is, the
# combination ('a', 'b') is considered to be the same as ('b', 'a') (which is not
# produced). For example:

from itertools import combinations

for c in combinations(items, 3):
    print(c)

for c in combinations(items, 2):
    print(c)

