# printing first prime no under a given number with the help of for loop.
n = int(input("enter a number:"))
for n in range(2, n + 1):
    count = 0
    for j in range(2, n // 2 + 1):
        if n % j == 0:
            count += 1
            break
    if count == 0:
        print(n)


















