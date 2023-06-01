# calculate factorial of a number.
total = 0
n = int(input("enter a natural number:"))
for i in range(1, n+1):
    total = total + n * n - 1
print(total)