# reverse a no using recursion.
def reverse_num(x):
    global reverse
    if x > 0:
        reverse = x % 10
        print(reverse, end='')
        return reverse_num(x // 10)


reverse = 0
x = int(input("enter a number:-"))
reverse_num(x)
