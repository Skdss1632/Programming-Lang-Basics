# script to print name of a person abbreviated form.
s = input("enter a string:-").split(' ')
for i in range(0, len(s) - 1):
    print(s[i][0], end='.')
print(s[len(s) - 1])
