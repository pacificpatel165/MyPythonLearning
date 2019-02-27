"""
Problem
You want to take a slice of data produced by an iterator, but the normal slicing operator
doesn’t work.
"""

# Solution
# The itertools.islice() function is perfectly suited for taking slices of iterators and
# generators. For example:

def Count(n):
    while True:
        yield n
        n += 1

c = Count(0)
# print(c[10:20]) #

# Iterators and generators can’t normally be sliced, because no information is known about
# their length (and they don’t implement indexing). The result of islice() is an iterator
# that produces the desired slice items, but it does this by consuming and discarding all
# of the items up to the starting slice index. Further items are then produced by the islice
# object until the ending index has been reached.

# Now using islice()

import itertools

for x in itertools.islice(c, 10, 20):
    print(x)
