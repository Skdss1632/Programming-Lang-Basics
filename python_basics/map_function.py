def cube(x):
    return x * x * x

print(cube(2))

l = [1,4,5,2]

newl = list(map(cube, l))
print(newl)