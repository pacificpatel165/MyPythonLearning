"""
Problem
You want a function to only accept certain arguments by keyword.
"""

# Solution
# This feature is easy to implement if you place the keyword arguments after a * argument
# or a single unnamed *. For example:

def recv(maxzise, *, block):
    print('Received a Message {} {}'.format(maxzise, block))
    pass


# recv(1024, True)      # TypeError
recv(1024, block=True)  # Ok


# This technique can also be used to specify keyword arguments for functions that accept
# a varying number of positional arguments. For example:

def mininum(*values, clip=None):
    m = min(values)
    if clip is not None:
        m = clip if clip < m else m
    return m


print(mininum(1, 5, 2, -5, 10))          # Returns -5
print(mininum(1, 5, 2, -5, 10, clip=-6))  # Returns -6

print(help(recv))
