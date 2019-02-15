"""
Problem
You need to create or test for the floating-point values of infinity, negative infinity, or
NaN (not a number).
"""

# Solution
# Python has no special syntax to represent these special floating-point values, but they
# can be created using float(). For example:

import math

a = float('inf')
print(a)
b = float('-inf')
print(b)
c = float('nan')
print(c)

# To test for the presence of these values, use the math.isinf() and math.isnan() functions.
# For example:

print(math.isinf(a))
print(math.isinf(b))
print(math.isnan(c))

# Infinite values will propagate in calculations in a mathematical manner. For example:
a = float('inf')
print(a + 45)
print(a * 10)
print(10 / a)

# However, certain operations are undefined and will result in a NaN result. For example:
a = float('inf')
print(a/a)
b = float('-inf')
print(a + b)

# NaN values propagate through all operations without raising an exception. For example:
c = float('nan')
print(c + 23)
print(c / 2)
print(c * 2)

# A subtle feature of NaN values is that they never compare as equal. For example:
c = float('nan')
d = float('nan')
print(c == d)
print(c is d)
