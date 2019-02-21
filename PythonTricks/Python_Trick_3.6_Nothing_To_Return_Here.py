# Python adds an implicit return  None statement to the end of any function.
# Therefore, if a function doesn't specify a return value,
# it return None by default.

def foo1(value):
    if value:
        return value
    else:
        return None


def foo2(value):
    """Bare retrun statement implies 'return None'"""
    if value:
        return value
    else:
        return


def foo3(value):
    """Missing return statement implies 'return None'"""
    if value:
        return value


print(type(foo1(0)))
print(type(foo2(0)))
print(type(foo3(0)))
