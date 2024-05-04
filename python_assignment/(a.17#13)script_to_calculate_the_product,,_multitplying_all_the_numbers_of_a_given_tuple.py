# script to calculate the product,multiplying all the numbers of a given tuple.
t1 = eval(input("enter a tuple:-"))
product = 1
for i in t1:
    product = product * i
print("product of given tuple is:-", product)