# class Car:
#     def __init__(self, model, colour, year):
#         self.model = model
#         self.colour = colour
#         self.year = year
#
#     def move(self):
#         print(f'{self.model} поехал')
#
#
# car1 = Car('bmw', 'black', '2021')
# car2 = Car('mersedes', 'white', '2022')
# #car1.move()
#
# print(car1.__dict__)
# print(Car.__dict__)


# class Circle:
#     def __init__(self, point, c):
#         self.center = point
#         self.radius = c
#
#
# def square(self):
#     return 3.14 * self.radius ** 2


# class Phone:
#     def __init__(self, model, colour, memory):
#         self.model = model
#         self.colour = colour
#         self.memory = memory
#         print(self.model, 'создан')
#
#     def __del__(self):
#         print(self.model, 'сломался')
#
# iphone = Phone('14 pro', 'purple', 512)
# del iphone


# class Vector:
#     MIN_COORD = 0
#     MAX_COORD = 100
#     @classmethod
#     def validate(cls, arg):
#         return cls.MIN_COORD <= arg <= cls.MAX_COORD
#
#     @staticmethod
#     def get_structure():
#         print('это вектор')


# v1 = Vector()
# print(Vector.MIN_COORD, v1.MIN_COORD)
# print(Vector.validate(5))
# v1.get_structure()


class Car:
    def __init__(self, model, colour, motor):
        self.model = model
        self._colour = colour
        self.__motor = motor


car1 = Car('bmw', 'black', 'v8')
print(car1._colour)