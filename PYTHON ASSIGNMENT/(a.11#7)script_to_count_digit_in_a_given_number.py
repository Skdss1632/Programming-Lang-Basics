# script to count digit in a given number.
x = int(input("enter a  number:"))
count = 0
while x > 0:
    x = x//10
    count += 1
print(count)