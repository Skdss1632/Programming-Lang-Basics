# printing next prime number of a given number with the help of for and while loop.
num = int(input("enter a number"))
while True:
    num += 1
    count = 0
    for i in range(2, num // 2 + 1):
        if num % i == 0:
            count += 1
    if count == 0:
        print(num)
        break












