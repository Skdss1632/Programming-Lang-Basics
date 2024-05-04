# creating a function that accepts a string and calculate no of uppercase and lowercase letters.
def total(str):
    count_upper = 0
    count_lower = 0
    for i in str:
        if i.isupper():
            count_upper += 1
        else:
            if i.islower():
                count_lower += 1
    print("total no of lower case letter is:-", count_lower)
    print("total no of upper case letter is:-", count_upper)



str = input("enter a string")
total(str)