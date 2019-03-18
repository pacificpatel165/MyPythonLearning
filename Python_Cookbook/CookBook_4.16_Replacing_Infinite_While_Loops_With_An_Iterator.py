"""
Problem
You have code that uses a while loop to iteratively process data because it involves a
function or some kind of unusual test condition that doesn’t fall into the usual iteration
pattern.
"""


# Solution
# A somewhat common scenario in programs involving I/O is to write code like this:

def process_data(data):
    pass


CHUNKSIZE = 8192


def reader(s):
    while True:
        data = s.recv(CHUNKSIZE)
        if data == b'':
            break
        process_data(data)


# Such code can often be replaced using iter(), as follows:

def reader(s):
    for chunk in iter(lambda: s.recv(CHUNKSIZE), b''):
        process_data(data)
