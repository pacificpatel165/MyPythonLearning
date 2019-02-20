# At their core, Python's decorators allow you to extend and modify the
# behaviour of a callable (functions, methids and classes) without
# permanently modifying the callable itself.

# Now, what are decorators really ? They "decorate" or "wrap" another
# function and let you execute code before and after the wrapped function runs.

def null_decorator(func):
    return func


def greet():
    return 'Hello!'


my_greet = null_decorator(greet)

print(my_greet)


@null_decorator
def greet():
    return 'Hello!!'


print(greet())


# ------------------------------------------------------
# Decorators Can Modify Behaviour
# ------------------------------------------------------
def uppercase(func):
    def wrapper():
        original_result = func()
        modified_result = original_result.upper()
        return modified_result

    return wrapper


@uppercase
def greet():
    return 'Hello Prashant !'


print(greet)
print(null_decorator(greet))
print(uppercase(greet))


# ------------------------------------------------------
# Applying Multiple Decorators To A Function
# ------------------------------------------------------
def strong(func):
    def wrapper():
        return '<strong>' + func() + '</strong>'

    return wrapper


def emphasis(func):
    def wrapper():
        return '<em>' + func() + '</em>'

    return wrapper


@strong
@emphasis
def greet():
    return 'Hello Prashant!'


print(greet())

# ------------------------------------------------------
# Decorating Functions That Accept Arguments
# ------------------------------------------------------
def trace(func):
    def wrapper(*args, **kwargs):
        print(f'TRACE: calling {func.__name__}() '
              f'with {args}, {kwargs}')

        original_result = func(*args, **kwargs)

        print(f'TRACE: {func.__name__}() '
              f'returned {original_result!r}')

        return original_result

    return wrapper

@trace
def say(name, line):
    return f'{name}: {line}'

print(say('Prashant', 'Hello World'))

# ------------------------------------------------------
# How To Write "Debuggable" Decorators
# ------------------------------------------------------

def greet():
    """Return a friendly greeting."""
    return 'Hello !'

decorated_greet = uppercase(greet)

print(greet.__name__)
print(greet.__doc__)

print(decorated_greet.__name__)
print(decorated_greet.__doc__)


import functools

def uppercase(func):
    @functools.wraps(func)
    def wrapper():
        return func().upper()

    return wrapper

@uppercase
def greet():
    """Retrun a friendly greeting."""
    return 'Hello !'

print(greet.__name__)
print(greet.__doc__)
