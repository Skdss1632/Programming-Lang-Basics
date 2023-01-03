# printing star pattern
# if n == 5
# * * * * *
# * * * *
# * * *
# * *
# *
n = int(input('enter a number:-'))
j = n
for i in range(1, n+1):
    j -= 1
    for k in range(1, j+2):
        print('*', end=' ')
    print()