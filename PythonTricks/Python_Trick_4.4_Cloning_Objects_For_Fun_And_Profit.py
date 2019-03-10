# Assignment statements in Python do not create copies of objects,
# they only bind names to an object. For immutable objects,
# that usually doesn't make a difference.

# Way to clone the object

# new_list = list(original_list)
# new_dict = dict(original_dict)
# new_set = set(original_set)

# Making Shallow Copies

xs = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
ys = list(xs)

xs.append(['new sublist'])
print(xs)
print(ys)

xs[1][0] = 'X'
print(xs)
print(ys)

# Making Deep Copies

import copy

xs = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
zs = copy.deepcopy(xs)
xs[1][0] = 'X'
print(xs)
print(zs)


# Shallow copy can be created using copy.copy()

# Copying Arbitrary Objects

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f'Point({self.x!r}, {self.y!r})'


a = Point(23, 45)
b = copy.copy(a)

print(a)
print(b)
print(a is b)


class Rectangle:
    def __init__(self, topleft, bottoright):
        self.topleft = topleft
        self.bottomright = bottoright

    def __repr__(self):
        return (f'Rectangle({self.topleft!r},'
                f' {self.bottomright!r})')


rect = Rectangle(Point(0, 1), Point(5, 6))
srect = copy.copy(rect)

print(rect)
print(srect)
print(rect is srect)

rect.topleft.x = 999
print(rect)
print(srect)

drect = copy.deepcopy(rect)
drect.topleft.x = 222
print(drect)
print(rect)
print(srect)
