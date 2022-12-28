# def a class to find square of a no and also count the no of times a function is called.
class Square:
    def __init__(self, num):
        self.num = num
        self.count = 0

    def set_num(self, x):
        self.num = x
        self.count += 1

    def display_square(self):
        print('square is:-', self.num ** 2, 'count is :-', s1.count)
        self.count += 1


s1 = Square(0)
s1.set_num(7)
s1.display_square()
