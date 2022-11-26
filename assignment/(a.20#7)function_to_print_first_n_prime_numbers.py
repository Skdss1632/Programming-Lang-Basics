# function to print first n prime numbers.
def prime(n):
    i = 2
    while n:
        count = 0
        for j in range(1, i+1):
            if i % j == 0:
                count += 1
        if count == 2:
            print(i)
            n -= 1
        i += 1


n = int(input("enter n number"))
prime(n)