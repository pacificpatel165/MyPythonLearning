"""
Problem
You want to iterate over items in an iterable, but the first few items aren’t of interest and
you just want to discard them.
"""

# Solution
# The itertools module has a few functions that can be used to address this task. The
# first is the itertools.dropwhile() function.

# To illustrate, suppose you are reading a file that starts with a series of comment lines.
# For example:

from itertools import dropwhile
with open('somefile.txt') as f:
    for line in dropwhile(lambda line: line.startswith('#'), f):
        print(line, end='')

from itertools import islice
items = ['a', 'b', 'c', 1, 4, 10, 15]
for x in islice(items, 3, None):
    print(x)
