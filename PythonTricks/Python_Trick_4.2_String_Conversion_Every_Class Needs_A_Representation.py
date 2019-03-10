# You can control to-string conversion in your own classes
# using the __str__ and __repr__ "dunder" methods.

# Always add a __repr___ to your classes. The default implementation
# for __str__ just call __repr__.

class Car:
    def __init__(self, color, mileage):
        self.color = color
        self.mileage = mileage


my_car = Car('red', 13131)
print(my_car)
print(repr(my_car))  # Or my_car


class Car:
    def __init__(self, color, mileage):
        self.color = color
        self.mileage = mileage

    def __repr__(self):
        return '__repr__ for Car'

    def __str__(self):
        return '__str__ for Car'


my_car = Car('red', 13131)
print(my_car)
print(repr(my_car))  # Or my_car


class Car:
    def __init__(self, color, mileage):
        self.color = color
        self.mileage = mileage

    def __repr__(self):
        return (f'{self.__class__.__name__}('
                f'{self.color!r}, {self.mileage!r})')

    def __str__(self):
        return f'a {self.color} Car'


my_car = Car('red', 13131)
print(my_car)
print(repr(my_car))  # Or my_car
