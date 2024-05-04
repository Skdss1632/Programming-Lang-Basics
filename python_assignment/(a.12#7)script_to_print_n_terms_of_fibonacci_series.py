# script to print n terms of fibonacci series.
n = int(input("enter a number:"))
a = 1
b = 0
while n:
    terms = a + b
    print(terms)
    n -= 1
    a = b
    b = terms

