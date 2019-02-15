"""
Problem
Your code for interacting with the latest web authentication scheme has encountered a
singularity and your only solution is to go around it in the complex plane. Or maybe
you just need to perform some calculations using complex numbers.
"""

# Solution
# Complex numbers can be specified using the complex(real, imag) function or by
# floating-point numbers with a j suffix.

a = complex(2, 4)

b = 3 - 5j

print(a)
print(b)
print(a.real, a.imag, a.conjugate())
print((a + b), (a - b), (a * b), (a / b), abs(a))

# To perform additional complex-valued functions such as sines, cosines, or square roots,
# use the cmath module:

import cmath

print(cmath.sin(a), cmath.cos(a), cmath.exp(a))

import numpy as np

a = np.array([2+3j, 4+5j, 6-7j, 8+9j])
print(a)
print(a+2)

import cmath
print(cmath.sqrt(-4))


