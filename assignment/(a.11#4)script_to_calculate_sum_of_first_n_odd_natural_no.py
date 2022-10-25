# script to calculate sum of first n odd natural number.
n = int(input("enter a natural number"))
i = 1
total = 0
while i <= n:
    total = total + i
    i += 2
print("sum of odd number of %d is %d" % (n, total))
