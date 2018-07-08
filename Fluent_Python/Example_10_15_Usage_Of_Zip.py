# coding=utf-8

"""The zip built-in at work."""
from itertools import zip_longest


print(zip(range(3), 'ABC'))

print(list(zip(range(3), 'ABC')))

print(list(zip(range(3), 'ABC', [0.0, 1.1, 2.2, 3.3])))

print(list(zip_longest(range(3), 'ABC', [0.0, 1.1, 2.2, 3.3], fillvalue=-1)))
