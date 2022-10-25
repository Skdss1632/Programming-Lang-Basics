# script to calculate sum of digit of a given number.
x = int(input("enter a natural number:"))
total = 0
while x > 0:
    total = (x % 10) + total
    x = x//10
print("sum of digits  is %d" % total)
