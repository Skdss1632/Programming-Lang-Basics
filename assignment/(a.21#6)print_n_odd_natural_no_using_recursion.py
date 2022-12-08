# function to printing n odd natural no using recursion.
def n_odd(n):
    if n == 0:
        return 0
    numbers = n + n_odd(n - 1)
    print("first n odd natural numbers are:-", 2*numbers-1)
    return 0


n = int(input("enter a number:"))
n_odd(n)