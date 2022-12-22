# define a class factorial and define an instance member function to find the factorial using class.
class Factorial:
    def __init__(self, num):
        self.num = num

    def get_num(self, num):
        if num == 1:
            return 1
        else:
            return num * self.get_num(num-1)

    def set_num(self, x):
        self.num = x


f1 = Factorial(0)
f1.set_num(4)
print(f1.get_num(7))
