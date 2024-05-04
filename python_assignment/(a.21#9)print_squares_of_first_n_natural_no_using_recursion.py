# printing squares of first n natural no using recursion.
def n_squares(n):
    if n == 0:
        return 0
    numbers = n + n_squares(n - 1)
    print("squares of first n natural numbers are:-", numbers**2)
    return 0


n = int(input("enter a number:"))
n_squares(n)