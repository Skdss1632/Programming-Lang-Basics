# function to  checking whether a given no is prime or not using recursion.
def is_prime(num):
    global count
    if num > 0:
        is_prime(num - 1)
        if i % num == 0:
            count += 1


count = 0
num = int(input("enter a number:-"))
i = num
is_prime(num)
if count == 2:
    print(num, "is a prime number")
else:
    print(num, "is a non-prime number")


