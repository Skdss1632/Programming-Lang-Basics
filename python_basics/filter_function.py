l = [1,2,4,6,4,3]
def filter_func(a):
    return a > 2

newl = list(filter(filter_func, l))
print(newl)