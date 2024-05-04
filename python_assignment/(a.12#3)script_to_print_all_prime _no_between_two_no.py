num1, num2 = int(input("enter first number:")), int(input("enter second number number:"))
for num1 in range(num1, num2+1):
    count = 0
    for num2 in range(2, num1//2+1):
        if num1 % num2 == 0:
            count += 1
            break
    if count == 0 and num1 > 1:
        print(num1, end=' ')







