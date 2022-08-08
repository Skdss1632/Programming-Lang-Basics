# to calculate even of first n even naturals numbers.
total = 0
n = int(input("enter a natural number:"))
for i in range(2, 2*n+1, 2):
    total = total + i
print(total)

       