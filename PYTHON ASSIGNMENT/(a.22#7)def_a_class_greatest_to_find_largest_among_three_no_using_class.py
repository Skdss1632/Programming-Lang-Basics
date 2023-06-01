# def a class greatest to find largest among three no using class.
class Largest:
    def __init__(self):
        self.num1 = 0
        self.num2 = 0
        self.num3 = 0

    def set_number(self):
        self.num1 = int(input("enter the first number:-"))
        self.num2 = int(input("enter the second number:-"))
        self.num3 = int(input("enter the third number:-"))

    def get_largest_number(self):
        if self.num1 > self.num2 and self.num1 > self.num3:
            return format(self.num1)
        if self.num2 > self.num1 and self.num2 > self.num3:
            return format(self.num2)
        else:
            return format(self.num3)


largest1 = Largest()
largest1.set_number()
print(largest1.get_largest_number())
