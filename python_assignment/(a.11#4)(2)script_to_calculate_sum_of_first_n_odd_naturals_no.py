# to calculate sum of first n odd naturals numbers.
total = 0
n = int(input("enter a natural number:"))
for i in range(1, 2*n, 2):
    total = total + i
print(total)