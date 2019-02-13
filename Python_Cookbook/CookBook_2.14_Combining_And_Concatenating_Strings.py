"""
Problem
You want to combine many small strings together into a larger string.
"""

# Solution
# If the strings you wish to combine are found in a sequence or iterable, the fastest way
# to combine them is to use the join() method.

parts = ['Is', 'Chicago', 'Not', 'Chicago?']
print(' '.join(parts))
print(','.join(parts))

a = 'Is Chicago'
b = 'Not Chicago?'
print(a + ' ' + b)
print('{} {}'.format(a, b))

a = 'Hello' 'World'
print(a)

data = ['ACME', 50, 91.1]
print(','.join(str(d) for d in data))