# function to calculating sum of first n even natural no using recursion.
def sum_even(n):
    if n == 0:
        return 0
    return 2*n+sum_even(n-1)


n = int(input("enter a number:-"))
total = sum_even(n)
print("sum of first n even natural no is:-", total)