# Count occurrences of needles in a haystack (same end result as Example 3-10).

haystack = set([1, 4, 5, 6, 8, 12, 15, 20, 21, 23, 23, 26, 29, 30])
needles = set([0, 1, 2, 5, 8, 10, 22, 23, 29, 30, 31])

found = 0
for n in needles:
    if n in haystack:
        found += 1

print("Is needle found = {}".format(found))