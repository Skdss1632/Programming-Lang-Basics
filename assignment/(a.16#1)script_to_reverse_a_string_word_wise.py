# script to reverse a string word wise.
s = input("enter a string:-").split(' ')
i = len(s)
while len(s):
    i -= 1
    print(s[i], end=' ')