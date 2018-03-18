# Count occurrences needles in a haystack ; these lines work for any iterable types.

haystack = [1, 4, 5, 6, 8, 12, 15, 20, 21, 23, 23, 26, 29, 30]
needles = [0, 1, 2, 5, 8, 10, 22, 23, 29, 30, 31]

found = len(set(needles) & set(haystack))
print("Is needle found = {}".format(found))

found = len(set(needles).intersection(haystack))
print("Is needle found = {}".format(found))

# Which method is faster
print("Which method is faster")

from dis import dis

print('Create set as ---> {1}')
print(dis('{1}'))
print('Create set as ---> set([1])')
print(dis('set([1])'))

print('frozenset(range(10))')
print(frozenset(range(10)))