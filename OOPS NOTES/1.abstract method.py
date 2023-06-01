from abc import ABC, abstractmethod


class Shape(ABC):
    # if we use abstractmethod and whatever fun has defined just below the absmthd
    # then we should also def exactly that name fun in another class
    @abstractmethod
    def printarea(self):
        return 0


class Rectangle(Shape):
    type = 'Rectangle'
    sides = 4

    def __init__(self):
        self.length = 6
        self.breadth = 7
    #
    # def printarea(self):
    #     return self.length * self.breadth


rect1 = Rectangle()