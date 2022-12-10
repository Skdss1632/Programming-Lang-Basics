# count digit in a given no using recursion.
def count_num(n):
    global count
    if n > 0:
        count += 1
        return count_num(n//10)


count = 0
n = int(input("enter a number:-"))
count_num(n)
print(count)