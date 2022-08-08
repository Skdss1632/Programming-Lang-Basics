# calculate factorial of a number.
total = 1
n = int(input("enter a natural number:"))
for i in range(1, n+1):
    total = total * i
print(total)