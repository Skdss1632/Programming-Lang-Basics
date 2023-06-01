# printing first n natural number in reverse order using recursion.
def natural(n):
    print("reverse n natural no are:-", n)
    if n == 1:
        return
    return natural(n-1)


n = int(input("enter a number:"))
natural(n)
