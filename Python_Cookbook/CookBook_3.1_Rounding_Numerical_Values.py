"""
Problem
You want to round a floating-point number to a fixed number of decimal places.
"""

# Solution
# For simple rounding, use the built-in round(value, ndigits) function.

print(round(1.23, 1))
print(round(1.27, 1))
print(round(-1.27, 1))
print(round(1.25361,3))

# The number of digits given to round() can be negative, in which case rounding takes
# place for tens, hundreds, thousands, and so on.
a = 1627731
print(round(a, -1))     # 1627730
a = 1627735
print(round(a, -1))     # 1627740

x = 1.23466
print(format(x, '0.2f'))    # '1.23'
print(format(x, '0.3f'))    # '1.235'


