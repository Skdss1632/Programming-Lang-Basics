x = int(input("enter a natural number:"))
total = 0
while x > 0:
    total = (x % 10) + total
    x = x//10
print("sum of digits  is %d" % total)
