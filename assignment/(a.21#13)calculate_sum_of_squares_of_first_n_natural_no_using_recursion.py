# function to calculate sum of squares of first n natural no using recursion.
def square(n):
    if n == 1:
        return 1
    return n**2+square(n-1)


n = int(input("enter a number:-"))
total = square(n)
print("sum of squares of n natural no is:-", total)