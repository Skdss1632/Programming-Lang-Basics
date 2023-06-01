# script to remove all non int values from a list.
l1 = eval(input("enter a list:-"))
l2 = [i for i in l1 if type(i) == int]
print("int values in list are:-", l2)






