"""
Problem
You need to perform the same operation on many objects, but the objects are contained
in different containers, and you’d like to avoid nested loops without losing the readability
of your code.
"""

# Solution
# The itertools.chain() method can be used to simplify this task. It takes a list of
# iterables as input, and returns an iterator that effectively masks the fact that you’re really
# acting on multiple containers. To illustrate, consider this example:

from itertools import chain

a = [1, 2, 3, 4]
b = ['x', 'y', 'z']

for x in chain(a, b):
    print(x)

# Inefficient
for x in a + b:
    pass

# Better
for x in chain(a, b):
    pass