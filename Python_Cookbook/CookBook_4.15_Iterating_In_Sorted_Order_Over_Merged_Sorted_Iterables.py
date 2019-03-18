"""
Problem
You have a collection of sorted sequences and you want to iterate over a sorted sequence
of them all merged together.
"""

# Solution
# The heapq.merge() function does exactly what you want. For example:

import heapq

a = [1, 4, 7, 10]
b = [2, 5, 6, 11]

for c in heapq.merge(a, b):
    print(c)

# The iterative nature of heapq.merge means that it never reads any of the supplied sequences
# all at once. This means that you can use it on very long sequences with very
# little overhead.


