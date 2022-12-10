# function to calculating sum of first n odd natural no using recursion.
def sum_odd(n):
    if n == 1:
        return 1
    return sum_odd(n-1)+2*n-1


n = int(input("enter a number:-"))
total = sum_odd(n)
print("sum of first n odd natural no is:-", total)