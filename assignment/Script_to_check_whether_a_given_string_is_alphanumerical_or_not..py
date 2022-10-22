# script to check whether a given string is alphanumeric or not.
s = input("enter a string:-")
no ='0 1 2 3 4 5 6 7 8 9'
for i in s:
    for j in no:
        if i == j:
            break
if i == j and s.count(' ') == 0:
    print("yes given string is alphanumeric")
else:
    print("no given string is not alphanumeric")