# calculating lcm of two numbers.
num1 = int(input("enter first number:"))
num2 = int(input("enter second number:"))
i = 1
while True:
    l1 = num1 * i
    for i in range(1, i+1):
        l2 = num2 * i
        if l1 == l2:
            break
    if l1 == l2:
        print(l2)
        break
    i += 1
