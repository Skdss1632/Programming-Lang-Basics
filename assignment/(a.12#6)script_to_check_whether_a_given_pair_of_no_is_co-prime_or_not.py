# script to check whether a given pair of no is co-prime or not.
num1, num2 = int(input("enter first number:")), int(input("enter second number number:"))
count = 0
for i in range(1, num1+num2//2+1):
    if num1 % i == 0 and num2 % i == 0:
        count += 1
if count == 1:
    print('co-prime')
else:
    print('non co-prime')





