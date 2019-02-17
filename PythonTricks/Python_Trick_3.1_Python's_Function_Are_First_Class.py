# Python's functions are first-class objects. You can assign them to
# variables, store them in data structures, pass then as arguments to
# other functions, and even return them as values from other functions

def yell(text):
    return text.upper() + '!'


print(yell('hello'))

# ------------------------------------------------------
# Functions Are Objects
# ------------------------------------------------------

bark = yell
print(bark('woof'))

# Let's delete yell function
del yell

# yell('hello?')
# NameError: name 'yell' is not defined

print(bark('hey'))
print(bark.__name__)

# ------------------------------------------------------
# Functions Can Be Stored In Data Structure
# ------------------------------------------------------
funcs = [bark, str.lower, str.capitalize]
print(funcs)

for f in funcs:
    print(f, f('hey there'))

print(funcs[0]('heyho'))


# ------------------------------------------------------
# Functions Can Be Passed To Other Functions
# ------------------------------------------------------
# Because functions are objects, you can pass then as arguments to
# other functions.

def greet(func):
    greeting = func('Hi, I am a Python program')
    print(greeting)


greet(bark)


def whisper(text):
    return text.lower() + '...'


greet(whisper)

# Functions that can accept  other functions as arguments are
# also called 'higher-order-functions'.

print(list(map(bark, ['hello', 'hey', 'hi'])))


# ------------------------------------------------------
# Functions Can Be Nested
# ------------------------------------------------------

def speak(text):
    def whisper(t):
        return t.lower() + '...'

    return whisper(text)


print(speak('Hello Prashant'))


def get_speak_func(volume):
    def whisper(text):
        return text.lower() + '...'

    def yell(text):
        return text.upper() + '!'

    if volume > 0.5:
        return yell
    else:
        return whisper


print(get_speak_func(0.3))
print(get_speak_func(0.8))

speak_func = get_speak_func(0.7)
print(speak_func('Hello'))


# ------------------------------------------------------
# Functions Can Capture Local State
# ------------------------------------------------------

def get_speak_func(text, volume):
    def whisper():
        return text.lower() + '...'

    def yell():
        return text.upper() + '!'

    if volume > 0.5:
        return yell
    else:
        return whisper


print(get_speak_func('Hello World', 0.7)())


def make_adder(n):
    def add(x):
        return x + n

    return add


plus_3 = make_adder(3)
plus_5 = make_adder(5)
print(plus_3(4))
print(plus_5(4))


# ------------------------------------------------------
# Objects Can Behave Like Functions
# ------------------------------------------------------
# While all functions are objects in Python, the reverse isn't true.
# Objects aren't functions. But they can be made 'callable', which
# allows you to treat them like functions in many cases


class Adder:
    def __init__(self, n):
        self.n = n

    def __call__(self, x):
        return self.n + x


plus_3 = Adder(3)
print(plus_3(4))

print(callable(plus_3))
print(callable(bark))
print(callable('hello'))
