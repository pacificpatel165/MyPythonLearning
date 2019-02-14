"""
Problem
You need to perform accurate calculations with decimal numbers, and don’t want the
small errors that naturally occur with floats.
"""

a = 4.2
b = 2.1
print(a + b)  # 6.300000000000001
print(a + b == 6.3)  # False

# These errors are a “feature” of the underlying CPU and the IEEE 754 arithmetic performed
# by its floating-point unit.
# If you want more accuracy (and are willing to give up some performance), you can use
# the decimal module:

from decimal import Decimal

a = Decimal('4.2')
b = Decimal('2.1')

print(a + b)
print((a + b) == Decimal('6.3'))

# A major feature of decimal is that it allows you to control different aspects of calculations,
# including number of digits and rounding. To do this, you create a local context
# and change its settings.

from decimal import localcontext

a = Decimal('1.3')
b = Decimal('1.7')
print(a / b)

with localcontext() as ctx:
    ctx.prec = 3
    print(a / b)

with localcontext() as ctx:
    ctx.prec = 50
    print(a / b)

nums = [1.23e+18, 1, -1.23e+18]
print(sum(nums))  # Notice how 1 disappears

import math

print(math.fsum(nums))
