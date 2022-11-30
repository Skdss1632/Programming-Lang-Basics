def print1(n):
    print("MYSIRG")
    if n > 1:
        return print1(n-1)


n = int(input("enter a no"))
print1(n)
