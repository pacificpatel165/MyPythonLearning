"""
Problem
You need to perform calculations on large numerical datasets, such as arrays or grids.
"""

# Solution
# For any heavy computation involving arrays, use the NumPy library. The major feature
# of NumPy is that it gives Python an array object that is much more efficient and better
# suited for mathematical calculation than a standard Python list.

# Python lists
x = [1, 2, 3, 4]
y = [5, 6, 7, 8]
print(x * 2)
# print(x + 10)

# Numpy arrays
import numpy as np

ax = np.array([1, 2, 3, 4])
ay = np.array([5, 6, 7, 8])

print(ax * 2)
print(ax + 10)
print(ax + ay)
print(ax * ay)


def f(x):
    return 3 * x ** 2 - 2 * x + 7


print(f(ax))

grid = np.zeros(shape=(1000, 1000), dtype=float)
print(grid)
print(grid + 10)

a = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
print(a)

# Select row 1
print(a[1])

# Select column 1
print(a[:,1])

# Select a subregion and change it
print(a[1:3, 1:3])
a[1:3, 1:3] += 10
print(a)

# Broadcast a row vector across an operation on all rows
print(a + [100, 101, 102, 103])

# Conditional assignment on an array
print(np.where(a < 10, a, 10))
