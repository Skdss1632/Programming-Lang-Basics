# to calculate sum of cubes first n natural numbers.
total = 0
n = int(input("enter a natural number:"))
for i in range(1, n+1):
    total = i * i * i
print(total)


