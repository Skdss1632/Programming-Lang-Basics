# script to create a list of first n prime numbers.
l1 = []
n = int(input("enter a number:-"))
i = 2
while n:
    count = 0
    for j in range(2, i//2+1):
        if i % j == 0:
            count += 1
            break
    if count == 0:
        l1.append(i)
        n -= 1
    i += 1
print("list of n prime number is:-", l1)






