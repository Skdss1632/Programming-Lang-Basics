# script to reverse a number.
x = int(input("enter a  number:"))
reverse = 0
while x > 0:
    reverse = reverse + x % 10
    x = x//10
print(reverse, end='')