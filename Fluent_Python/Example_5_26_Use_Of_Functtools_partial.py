# coding=utf-8


""""Using partial to use a 2-argument function where a 1-argument calla‐ble is required."""

from operator import mul
from functools import partial


triple = partial(mul, 3)
print(triple(7))

print(list(map(triple, range(1, 10))))


