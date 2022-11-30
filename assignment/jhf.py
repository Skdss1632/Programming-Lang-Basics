def total(a, b):
    if a <= b:
        a = + 1
        return a**2
    return total(n-1)


n = int(input("enter a no:-"))
result = total(1, n)
print(result)