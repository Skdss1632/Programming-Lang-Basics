# script to sort (ascending and descending) a dict by value.
dict1 = eval(input("enter a dict:-"))
sorted1 = sorted(dict1.values())
print("sorted list of dict in ascending order is:-", sorted1)
print("sorted list of dict in descending order is:-", sorted1[::-1])