"""
Problem
You have entered a time machine and suddenly find yourself working on elementarylevel
homework problems involving fractions. Or perhaps you’re writing code to make
calculations involving measurements made in your wood shop.
"""

# Solution
# The fractions module can be used to perform mathematical calculations involving
# fractions. For example:

from fractions import Fraction

a = Fraction(5, 4)
b = Fraction(7, 16)

print(a + b)
print(a * b)

# Getting numerator/denominator
c = a * b
print(c.numerator)
print(c.denominator)

# Converting to a float
print(float(c))

# Limiting the denominator of a value
print(c.limit_denominator(8))

# Converting a float to a fraction
x = 3.75
y = Fraction(*x.as_integer_ratio())
print(y)
