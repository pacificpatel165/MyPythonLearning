# Single Leading Underscore "_var":
# Naming convention indicating a name is meant for internal use.
# A hint for programmers and not enforced by the interpreter
# ( except in wildcard imports).

# Single Trailing Underscore "var_":
# Used by convention to avoid naming conflicts with Python keywords.

# Double Leading Underscore "__var":
# Triggers name mangling when used in a class context. Enforced
# by the Python interpreter.

# Double Leading and Trailing Underscore "__var__":
# Indicated special methods defined by the Python languages.
# Avoid this naming scheme for your own attribute

# Single Underscore "_":
# Sometimes used as a name for temporary or insignificant variables
# ("don't care"). Also, it represents the result of the last
# expression in a Python REpL session.


# ---------------------------------
# Single Leading Underscore "_var":
# ---------------------------------

class Test:
    def __init__(self):
        self.x = 11
        self._y = 23


t = Test()
print(t.x)
print(t._y)


# Note : 'from my_module import *' will not able access the private(_) functions and variables.


# ----------------------------------
# Single Trailing Underscore "var_":
# ----------------------------------

# def make_object(name, class):
#    'SyntaxError: "invalid syntax"

def make_object(name, class_):
    pass


# ----------------------------------
# Double Leading Underscore "__var":
# ----------------------------------

# A double underscore prefix causes the Python interpreter to rewrite
# the attribute name in order ti avoid naming conflicts in subclasses

class Test:
    def __init__(self):
        self.foo = 11
        self._bar = 12
        self.__baz = 13


t = Test()
print(dir(t))
# ['_Test__baz', '__class__', ... '_bar', 'foo']
# print(t.__baz)
print(t._Test__baz)  # It's rewrite the __baz variable to _Test_baz

_MangledGlobal__mangled = 23


class MangledGlobal:
    def test(self):
        return __mangled


print(MangledGlobal().test())

# -------------------------------------------------
# Double Leading and Trailing Underscore "__var__":
# -------------------------------------------------

# In short, Double underscore are called "dunders"

class PrefixPostfixTest:
    def __init__(self):
        self.__bam__ = 42

print(PrefixPostfixTest().__bam__)

# ----------------------
# Single Underscore "_":
# ----------------------

for _ in range(3):
    print('Hello Prashant')

car = ('red', 'auto', 12, 313.14)
color, _, _, mileage = car
print(color, mileage)

import this
print(this)

