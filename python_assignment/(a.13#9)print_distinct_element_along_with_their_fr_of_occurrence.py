# print_distinct_element_along_with_their_frequency_of_occurrence.py
l1 = eval(input("enter a list"))
for i in range(min(l1), max(l1)+1):
    f = l1.count(i)
    if f > 0:
        print("frequency of %d is %d" % (i, f))









