# script to check if a given value is present in a set or not.
setx = eval((input("enter a set:-\n")))
value = int(input("enter a value:-\n"))
if value in setx:
    print("yes given value is present in given set")
else:
    print("no given value is not present in a given set")
