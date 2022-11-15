# script to check whether a given key already exist in a dict.
dict1 = eval(input("enter a dict:-"))
key = int(input("enter a key"))
if key in dict1:
    print("yes given key is present in given dict ")
else:
    print("no given key is present in given dict")