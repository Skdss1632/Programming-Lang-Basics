# function to printing first 10 multiple of 5 using recursion.
def num(x):
    if x == 0:
        return 0
    multiple = 5*x+num(x-1)
    print("first 10 multiple of 5 is:-", multiple)
    return 0


num(10)