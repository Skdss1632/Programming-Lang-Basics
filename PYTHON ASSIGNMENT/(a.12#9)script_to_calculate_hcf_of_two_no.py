# calculating hcf of two numbers.
num1 = int(input("enter first number:"))
num2 = int(input("enter second number:"))
for i in range(2, num1 + num2//2+1):
    if num1 % i == 0 and num2 % i == 0:
        h = i
    if i == num1 + num2 // 2:
        print(h)










