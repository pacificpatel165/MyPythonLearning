"""
Problem
You want to return multiple values from a function.
"""


# Solution
# To return multiple values from a function, simply return a tuple. For example:

def myfun():
    return 1, 2, 3


a, b, c = myfun()
print(a, b, c)

a = (1, 2)  # With parentheses
print(a)
b = 1, 2    # Without parentheses
print(b)
