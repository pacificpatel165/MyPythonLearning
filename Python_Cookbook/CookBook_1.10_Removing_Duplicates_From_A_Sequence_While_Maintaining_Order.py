"""
Problem
You want to eliminate the duplicate values in a sequence, but preserve the order of the
remaining items.
"""


# If the values in the sequence are hashable, the problem can be easily solved using a set
# and a generator.

def dedupe(items):
    seen = set()
    for item in items:
        if item not in seen:
            yield item
            seen.add(item)


a = [1, 5, 2, 1, 9, 1, 5, 10]
print(list(dedupe(a)))


# If you are trying to eliminate
# duplicates in a sequence of unhashable types (such as dicts),

def dedupe_unhashable(items, key=None):
    seen = set()
    for item in items:
        val = item if key is None else key(item)
        if val not in seen:
            yield item
            seen.add(val)


a = [{'x': 1, 'y': 2}, {'x': 1, 'y': 3}, {'x': 1, 'y': 2}, {'x': 2, 'y': 4}]
print(list(dedupe_unhashable(a, key=lambda d: (d['x'], d['y']))))
print(list(dedupe_unhashable(a, key=lambda d: d['x'])))