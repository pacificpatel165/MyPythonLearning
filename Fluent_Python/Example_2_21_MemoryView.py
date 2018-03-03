# Changing the value of an array item by poking one of its bytes.

import array

numbers = array.array('h', [-2, -1, 0, 1, 2])
memv = memoryview(numbers)
print(len(memv))
print(memv[0])

memv_oct = memv.cast('B')  # Create memv_oct by casting the elements of memv to typecode 'B' (unsigned char).
print(memv_oct.tolist())
memv_oct[5] = 4
print(numbers)
