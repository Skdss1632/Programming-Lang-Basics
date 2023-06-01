# script to reverse each word in the string.
s = input("enter a string:-").split(' ')
for i in range(0, len(s)):
    e = s[i]
    print(e[::-1], end=' ')