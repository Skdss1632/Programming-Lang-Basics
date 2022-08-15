# printing first prime no under a given number.
x = int(input("enter a number"))
prime = 2
while prime <= x:
    i = 2
    count = 0
    while i <= prime//2:
        if prime % i == 0:
            count += 1
            break
        i += 1
    if count == 0:
        print(prime)
    prime += 1
