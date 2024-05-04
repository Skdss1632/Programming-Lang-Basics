# script to modify the first item (22) of a list inside a following tuple to 222.
t1 = (11, [22, 33], 44, 55)
t1 = t1[1][0] + 200
print("modified tuple is :-", t1)