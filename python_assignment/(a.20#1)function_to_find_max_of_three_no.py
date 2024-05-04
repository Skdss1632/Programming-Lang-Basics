# function to find max of three no.
def num(a, b, c):
    if a > b > c:
        print(a, "is greater among three")
    elif b > a and b > c:
        print(b, "is greater  among three")
    else:
        print(c, "is greater  among three")


num(1057, 8660, 860)

