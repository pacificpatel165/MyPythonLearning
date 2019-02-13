"""
Problem
You need to format text with some sort of alignment applied.
"""

# Solution
# For basic alignment of strings, the ljust(), rjust(), and center() methods of strings
# can be used.

text = 'Hello World'

print(text.ljust(20))
print(text.rjust(20))
print(text.center(20))
print(text.rjust(20,'='))
print(text.center(20, '*'))

# The format() function can also be used to easily align things. All you need to do is use
# the <, >, or ^ characters along with a desired width.

print(format(text, '>20'))
print(format(text, '<20'))
print(format(text, '^20'))

# If you want to include a fill character other than a space, specify it before the alignment
# character:

print(format(text, '=>20s'))
print(format(text, '*^20s'))

# These format codes can also be used in the format() method when formatting multiple
# values

print('{:>10s} {:>10s}'.format('Hello', 'World'))

x = 1.2345
print(format(x, '>10'))
print(format(x, '^10.2f'))
