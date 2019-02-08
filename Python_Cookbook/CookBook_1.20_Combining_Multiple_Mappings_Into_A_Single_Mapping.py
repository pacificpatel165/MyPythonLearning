"""
Problem
You have multiple dictionaries or mappings that you want to logically combine into a
single mapping to perform certain operations, such as looking up values or checking
for the existence of keys.
"""

# Solution
# An easy way to do this is to use the
# ChainMap class from the collections module.

from collections import ChainMap

a = {'x': 1, 'z': 3}
b = {'y': 6, 'z': 8}

c = ChainMap(a, b)
print(c['x'])       # Outputs 1 (from a)
print(c['y'])       # Outputs 2 (from b)
print(c['z'])       # Outputs 3 (from a)
print(len(c))
print(list(c.keys()))
print(list(c.values()))
print(list(c.items()))

# Operations that mutate the mapping always affect the first mapping listed.
c['z'] = 10
c['w'] = 20
del c['x']
print(a)
# del c['y'] # KeyError: "Key not found in the first mapping: 'y'"

a = {'x': 1, 'z': 3 }
b = {'y': 2, 'z': 4 }

merged = dict(b)
merged.update(a)
print(list(merged.items()))

# If any of the original dictionaries
# mutate, the changes don’t get reflected in the merged dictionary
a['x'] = 7
print(list(merged.items()))

