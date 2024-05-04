# def a class rectangle and define an instance member function to find the area of rectangle.
class Rectangle:
    def __init__(self):
        self.length = 0
        self.breadth = 0

    def set_num(self):
        self.length = int(input("enter the length:--"))
        self.breadth = int(input("enter the breadth:--"))

    def area_of_rectangle(self):
        print('area of rectangle is:--', self.length * self.breadth)


rectangle1 = Rectangle()
rectangle1.set_num()
rectangle1.area_of_rectangle()