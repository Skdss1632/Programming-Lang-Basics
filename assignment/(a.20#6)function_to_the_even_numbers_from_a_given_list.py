# function to the even numbers from a given list.
def check(list1):
    even_list = []
    for i in list1:
        if i % 2 == 0:
            even_list.append(i)
    print(even_list)


list1 = eval(input("enter a list"))
check(list1)