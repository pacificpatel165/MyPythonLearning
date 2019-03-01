"""
Problem
You want to iterate over a sequence, but would like to keep track of which element of
the sequence is currently being processed.
"""

# Solution
# The built-in enumerate() function handles this quite nicely:

my_list = ['a', 'b', 'c']
for idx, val in enumerate(my_list):
    print(idx, val)

my_list = ['a', 'b', 'c']
for idx, val in enumerate(my_list, 1):
    print(idx, val)
