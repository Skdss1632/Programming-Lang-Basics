# script to print first n prime number with the help of for and while loop.
n = int(input("enter a number:"))
i = 2
while n:
    count = 0
    for j in range(2, i // 2 + 1):
        if i % j == 0:
            count += 1
            break
    if count == 0:
        print(i)
        n -= 1
    i += 1


















