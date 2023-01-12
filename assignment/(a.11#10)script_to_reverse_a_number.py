# script to reverse a number
x = int(input("enter a  number:"))
while x > 0:
    reverse = x % 10
    x = x//10
    print(reverse, end='')