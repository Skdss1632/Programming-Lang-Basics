# def a class and def an instance member function to find the area of the circle.
class Circle:
    pi_value = 3.14

    def __init__(self):
        self.radius = 0

    def set_area_value(self):
        self.radius = int(input('enter a radius:-'))

    def area_of_circle(self):
        print('area of circle is:-', self.pi_value * self.radius ** 2)


circle1 = Circle()
circle1.set_area_value()
circle1.area_of_circle()





