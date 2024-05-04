# function to check whether a number falls in a given range or not.
def check_range(num):
    if num in range(lower_value, upper_value):
        print("yes")
    else:
        print("no")


num = int(input("enter a no"))
lower_value = int(input("enter a lower value"))
upper_value = int(input("enter a upper value"))
check_range(num)