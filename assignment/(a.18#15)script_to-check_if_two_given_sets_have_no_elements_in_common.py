# script to check if two given sets have no elements in common.
setx = eval(input("enter 1st set:-\n"))
sety = eval(input("enter 2nd set:-\n"))
for e in setx:
    if e in sety:
        print(e, "is the common element")