# coding=utf-8


""""Factorial implemented with reduce and an anonymous function."""

from functools import reduce


def fact(n):
    return reduce(lambda a, b: a * b, range(1, n + 1))

print(fact(5))
