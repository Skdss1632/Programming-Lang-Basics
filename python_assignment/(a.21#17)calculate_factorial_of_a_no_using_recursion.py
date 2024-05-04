# function to calculating factorial of a no using recursion.
def factorial(n):
    if n == 1:
        return 1
    return n*factorial(n-1)


n = int(input("enter a number:-"))
total = factorial(n)
print("factorial of given n number is:--", total)