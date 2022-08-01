n = int(input("enter a natural number:"))
i = 1
total = 0
while i <= n:
    total = total + 2*i
    i += 1
print("sum of even number of %d is %d" % (n, total))
