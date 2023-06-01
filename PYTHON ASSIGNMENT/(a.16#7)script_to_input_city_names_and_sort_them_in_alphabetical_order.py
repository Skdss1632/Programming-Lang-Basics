# script to input city names and sort them in alphabetical order.
s1 = input("enter a string:-")
s2 = sorted(s1)
for i in range(s2.count(' '), len(s2)):
    print(s2[i], end='')

