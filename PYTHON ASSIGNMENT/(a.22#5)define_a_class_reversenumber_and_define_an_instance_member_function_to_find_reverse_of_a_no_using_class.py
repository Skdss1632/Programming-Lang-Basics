# define a class reversenumber and define an instance member function to find reverse of a no using class.
class Reversenumber:
    def __init__(self):
        self.num = 0

    def set_num(self, x):
        self.num = x

    def get_num(self, num):
        if num > 0:
            reverse = num % 10
            print(reverse, end='')
            return self.get_num(num // 10)


reverse_num1 = Reversenumber()
reverse_num1.set_num(246)
reverse_num1.get_num(reverse_num1.num)