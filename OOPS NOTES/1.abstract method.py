from abc import ABC, abstractmethod


class Shape(ABC):
    """if we use abstractmethod and whatever fun has defined just above we have to use the decorator abstractmethod
    then we should also define the exactly same name of  fun in another class"""

    @abstractmethod
    def print_area(self):
        return 0


class Rectangle(Shape):
    type = 'Rectangle'
    sides = 4

    def __init__(self):
        self.length = 6
        self.breadth = 7
    #
    # def print_area(self):
    #     return self.length * self.breadth


rect1 = Rectangle()