"""
Problem
You need to supply a short callback function for use with an operation such as sort(),
but you don’t want to write a separate one-line function using the def statement. Instead,
you’d like a shortcut that allows you to specify the function “in line.”
"""

# Solution
# Simple functions that do nothing more than evaluate an expression can be replaced by
# a lambda expression. For example:

add = lambda x, y: x + y
print(add(2, 3))
print(add('hello', 'world'))
