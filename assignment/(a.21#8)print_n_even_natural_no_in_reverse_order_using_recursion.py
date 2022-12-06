# printing n even natural no in reverse order using recursion.
def even(n):
    print("reverse order of n even natural no are:-", 2*n)
    if n == 1:
        return
    return even(n-1)


n = int(input("enter a number:"))
even(n)
