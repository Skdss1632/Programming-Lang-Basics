# script to calculate sum of first n natural numbers.
n = int(input("enter a natural number:"))
total = 0
i = 1
while i <= n:
    total = total + i
    i += 1
print("sum of %d is %d" % (n, total))
