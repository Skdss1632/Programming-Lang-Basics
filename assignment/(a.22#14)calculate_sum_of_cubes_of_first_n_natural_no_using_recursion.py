# function to calculating sum of cubes of first n natural no using recursion.
def cubes(n):
    if n == 1:
        return 1
    return n**3+cubes(n-1)


n = int(input("enter a number:-"))
total = cubes(n)
print("sum of squares of n natural no is:-", total)