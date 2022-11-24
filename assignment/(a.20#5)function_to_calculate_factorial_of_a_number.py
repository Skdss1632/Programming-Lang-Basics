# function to calculate factorial of a number.
def factorial(num):
    total = 1
    for i in range(1, num+1):
        total = total * i
    return total


num = int(input("enter a number:-"))
factorial = factorial(num)
print("factorial of", num, "is:-", factorial)