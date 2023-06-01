# script to multiply all the items in a dict.
dict1 = eval(input("enter a dict\n"))
product = 1
for k in dict1.keys():
    product = product * k
print("product of given item in a given dict is\n", product)
