# coding=utf-8


""""Factorial implemented with reduce and operator.mul ."""

from functools import reduce
from operator import mul


def fact(n):
    return reduce(mul, range(1, n+1))

print(fact(5))
