# coding=utf-8


""""Sum of integers up to 99 performed with reduce and sum."""

# Starting with Python 3.0, reduce is not a built-in.
from functools import reduce

# Import add to avoid creating a function just to add two numbers.
from operator import add

# Sum integers up to 99.
print(reduce(add, range(100)))

# Same task using sum; import or adding function not needed.
print(sum(range(100)))
