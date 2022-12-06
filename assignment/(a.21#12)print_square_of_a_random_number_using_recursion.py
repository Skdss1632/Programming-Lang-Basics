# print square of a random number using recursion.
def total(n):
    if n == 5:
        return n**2
    total(n-1)


result = total(5)
print(result)