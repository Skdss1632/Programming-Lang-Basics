# function to calculating sum of digits of a given no using recursion.
total = 0


def sum_digits(x):
    global total
    if x > 0:
        total = x % 10 + total
        return sum_digits(x // 10)


x = int(input("enter a number:-"))
sum_digits(x)
print(" sum of digits of a given no is:-", total)