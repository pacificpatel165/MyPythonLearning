# The 'with' is statement which make sure that destruction/closing must called

with open('hello.txt', 'w') as f:
    f.write('Hello, World!')

# Or alternatively we can use as below

f = open('hello.txt', 'w')
try:
    f.write('hello world')
finally:
    f.close()


# Supporting 'with' in Your Own Objects
# What's a context manager ? It's a simple "protocol"(or interface)
# that your object needs to follow in order to support the 'with'
# statement. Basically, all you need to do is add __enter__ and
# __exit__ methods to an object if you want it to function as as
# context manager.

class ManagedFile:
    def __init__(self, name):
        self._name = name

    def __enter__(self):
        self._file = open(self._name, 'w')
        return self._file

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self._file:
            self._file.close()


with ManagedFile('hello.txt') as f:
    f.write('Hello Prashant!\n')
    f.write('Bye now')

# We can also use 'contextlib' utility module to makes life easier

from contextlib import contextmanager


@contextmanager
def managed_file(name):
    try:
        f = open(name, 'w')
        yield f
    finally:
        f.close()


with managed_file('hello.txt') as f:
    f.write('Hello Patel!\n')
    f.write('Bye now !!')
