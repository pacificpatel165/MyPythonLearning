"""
Problem
You want to iterate over the items contained in more than one sequence at a time.
"""

# Solution
# To iterate over more than one sequence simultaneously, use the zip() function. For
# example:

xpts = [1, 5, 4, 2, 10, 7]
ypts = [101, 78, 37, 15, 62, 99]

for x, y in zip(xpts, ypts):
    print(x, y)

# Iteration stops whenever one of the input sequences is
# exhausted. Thus, the length of the iteration is the same as the length of the shortest
# input. For example:

a = [1, 2, 3]
b = ['w', 'x', 'y', 'z']

for i in zip(a, b):
    print(i)

# If this behavior is not desired, use itertools.zip_longest() instead. For example:

from itertools import zip_longest

for i in zip_longest(a, b):
    print(i)

for i in zip_longest(a, b, fillvalue=0):
    print(i)

headers = ['name', 'shares', 'price']
values = ['ACME', 100, 490.1]

s = dict(zip(headers, values))
print(s)

a = [1, 2, 3]
b = [10, 11, 12]
c = ['x', 'y', 'z']

for i in zip(a, b, c):
    print(i)

# zip() creates an iterator as a result.
# If you need the paired values stored in a list, use the list() function. For example:
print(zip(a, b))
print(list(zip(a, b)))
