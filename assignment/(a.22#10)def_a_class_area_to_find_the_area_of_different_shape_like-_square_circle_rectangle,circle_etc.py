# def a class area and def instance member function to find the area of the different shape like-circle,square,rectangle
class Area:
    pi_value = 3.14

    def __init__(self):
        self.side = 0
        self.length = 0
        self.breadth = 0
        self.radius = 0

    def set_square_side_value(self):
        self.side = int(input("enter side value:-"))

    def set_rectangle_value(self):
        self.length = int(input("enter the length value:-"))
        self.breadth = int(input("enter the breadth value:-"))

    def set_circle_value(self):
        self.radius = int(input("enter the radius:-"))

    @property
    def get_area_of_circle(self):
        return format(self.pi_value * self.radius ** 2)

    @property
    def get_area_of_square(self):
        return format(4 * self.side)

    @property
    def get_area_of_rectangle(self):
        return format(self.length * self.breadth)


square1 = Area()
rectangle1 = Area()
circle1 = Area()
circle1.set_circle_value()
print(circle1.get_area_of_circle)








