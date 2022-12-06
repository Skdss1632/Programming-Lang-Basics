# print cubes of n natural number using recursion.
def n_cubes(n):
    if n > 0:
        n_cubes(n - 1)
        print("squares of first n natural numbers are:-", n ** 3)


n = int(input("enter a number:"))
n_cubes(n)