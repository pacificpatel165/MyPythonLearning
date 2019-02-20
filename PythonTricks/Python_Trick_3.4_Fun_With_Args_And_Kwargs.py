# This i about *args and **kwargs

def foo(required, *args, **kwargs):
    print(required)
    if args:
        print(args)
    if kwargs:
        print(kwargs)


print(foo('hello'))
print(foo('hello', 1, 2, 3))
print(foo('hello', 1, 2, 3, key1='value', key2=999))
