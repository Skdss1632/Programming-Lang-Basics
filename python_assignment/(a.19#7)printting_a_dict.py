# script to print a dict where the keys are no b/w 1 to n in the form of (x, x*x)
n = int(input("enter a no\n"))
dict1 = {}
for i in range(1, n+1):
    dict1[i] = i * i
print(dict1)