n = int(input("enter a natural number:"))
total = 1
i = 1
while i <= n:
    total = total + i
    i += 1
print("squares of %d is %d" % (n, total))
