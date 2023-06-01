# print first n even natural number using recursion.
def n_even(n):
    if n == 0:
        return 0
    numbers = n + n_even(n - 1)
    print("first n even natural numbers are:-", 2*numbers)
    return 0


n = int(input("enter a number:"))
n_even(n)