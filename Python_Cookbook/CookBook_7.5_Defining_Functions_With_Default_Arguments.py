"""
Problem
You want to define a function or method where one or more of the arguments are
optional and have a default value.
"""


# Solution
# On the surface, defining a function with optional arguments is easy—simply assign
# values in the definition and make sure that default arguments appear last. For example:

def spam(a, b=42):
    print(a, b)


spam(1)  # Ok. a=1, b=42
spam(1, 2)  # Ok. a=1, b=2


# If the default value is supposed to be a mutable container, such as a list, set, or dictionary,
# use None as the default and write code like this:

# Using a list as a default value
def spam(a, b=None):
    if b is None:
        pass
    pass


_no_value = object()


def spam(a, b=_no_value):
    if b is _no_value:
        print('No b value supplied')


spam(1)
spam(1, 2)  # b = 2
spam(1, None)  # b = None

# First, the values assigned as a default are bound only once at the time of function definition.
# Try this example to see it:

x = 42


def spam(a, b=x):
    print(a, b)


spam(1)

x = 36
spam(7)
