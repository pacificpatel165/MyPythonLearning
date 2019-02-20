"""
Problem
You want to pick random items out of a sequence or generate random numbers.
"""

# Solution
# The random module has various functions for random numbers and picking random
# items. For example, to pick a random item out of a sequence, use random.choice():

import random

values = [1, 2, 3, 4, 5, 6]

print(random.choice(values))
print(random.choice(values))

# To take a sampling of N items where selected items are removed from further consideration,
# use random.sample() instead:

print(random.sample(values, 2))
print(random.sample(values, 2))

# If you simply want to shuffle items in a sequence in place, use random.shuffle():
random.shuffle(values)
print(values)

# To produce random integers, use random.randint():
print(random.randint(0, 10))

# To produce uniform floating-point values in the range 0 to 1, use random.random():
print(random.random())

# To get N random-bits expressed as an integer, use random.getrandbits():
print(random.getrandbits(200))


# The random module computes random numbers using the Mersenne Twister algorithm.
# This is a deterministic algorithm, but you can alter the initial seed by using the
# random.seed() function. For example:

random.seed()               # Seed based on system time or os.urandom()
random.seed(12345)          # Seed based on integer given
random.seed(b'bytedata')    # Seed based on byte data

