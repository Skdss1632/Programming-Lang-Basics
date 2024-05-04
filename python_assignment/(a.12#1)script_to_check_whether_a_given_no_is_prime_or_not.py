# script to check whether a given no is prime or not.
num = int(input("enter a number"))
count = 0
for i in range(2, num//2+1):
    if num % i == 0:
        count += 1
        break
if count == 0:
    print('given no is prime no')

else:
    print('given no is non-prime')

