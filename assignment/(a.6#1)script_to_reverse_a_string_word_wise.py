# script to reverse a string word wise.
s = input("enter a string:-").split(' ')
i = len(s)
while i:
    i -= 1
    reverse = s[i]
    print(reverse)
