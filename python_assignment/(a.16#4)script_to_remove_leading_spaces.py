# script_to_remove_leading_spaces.
s = input("enter a string:-")
for i in s:
    if i > min(' '):
        print(i, end='')
