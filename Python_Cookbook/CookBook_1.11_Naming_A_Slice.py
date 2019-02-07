"""
Problem
Your program has become an unreadable mess of hardcoded slice indices and you want
to clean it up.
"""

items = [0, 1, 2, 3, 4, 5, 6]
print(items[2:4])
a = slice(2, 4)
print(items[a])

items[a] = [10, 11]
print(items)

del items[a]
print(items)

# We can use slice as looping like start, stop and step
a = slice(3, 50, 2)
print(a.start)
print(a.stop)
print(a.step)

# You can map a slice onto a sequence of a specific size by using its indi
# ces(size) method.

s = 'HelloWorld'
print(a.indices(len(s)))
for i in range(*a.indices(len(s))):
    print(s[i])