"""
Problem
You have data inside of a sequence, and need to extract values or reduce the sequence
using some criteria.
"""

mylist = [1, 4, -5, 10, -7, 2, 3, -1]

print([n for n in mylist if n > 0])

# One potential downside of using a list comprehension is that it might produce a large
# result if the original input is large.

pos = (n for n in mylist if n > 0)
print(pos)

for x in pos:
    print(x)

values = ['1', '2', '-3', '-', '4', 'N/A', '5']

def is_int(val):
    try:
        x = int(val)
        return True
    except ValueError:
        return False

print(list(filter(is_int, values)))