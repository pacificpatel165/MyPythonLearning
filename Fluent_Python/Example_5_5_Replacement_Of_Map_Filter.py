# coding=utf-8

"""The map and filter functions are still builtins in Python 3, but since the introduction of list
comprehensions and generator expressions, they are not as important.

Lists of factorials produced with map and filter compared to alternatives coded as list comprehensions"""


def factorial(n):
    """returns n!"""
    return 1 if n < 2 else n * factorial(n - 1)


fact = factorial

# Build a list of factorials from 0! to 5!
print(list(map(fact, range(6))))

# Same operation, with a list comprehension.
print([fact(n) for n in range(6)])

# List of factorials of odd numbers up to 5!, using both map and filter.
print(list(map(fact, filter(lambda n: n % 2, range(6)))))

# List comprehension does the same job, replacing map and filter, and making lambda unnecessary
print([fact(n) for n in range(6) if n % 2])
