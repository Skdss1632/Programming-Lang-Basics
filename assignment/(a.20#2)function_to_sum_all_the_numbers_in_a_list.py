# function to sum all the numbers in a list.
def sum1(list1):
    total = 0
    for i in range(0, len(list1)):
        total = total + list1[i]
    print("sum of all the elements is:-", total)


list1 = [5, 4, 2]
sum1(list1)
