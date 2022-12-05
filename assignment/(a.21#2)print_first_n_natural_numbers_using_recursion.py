# printing first n natural number using recursion.
def n_natural(n):
    if n == 0:
        return 0
    numbers = n+n_natural(n - 1)
    print("first n natural numbers are:-", numbers)
    return 0


n = int(input("enter a number:"))
n_natural(n)
