# reverse a no using recursion.
def reverse_num(x):

    if x > 0:
        reverse = x % 10
        print(reverse, end='')
        return reverse_num(x // 10)


x = int(input("enter a number:-"))
reverse_num(x)
