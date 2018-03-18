# Count occurrences needles in a haystack , both of type set

haystack = set([1, 4, 5, 6, 8, 12, 15, 20, 21, 23, 23, 26, 29, 30])
needles = set([0, 1, 2, 5, 8, 10, 22, 23, 29, 30, 31])

found = len(needles & haystack)
print("Is needle found = {}".format(found))