# star pattern printing
# if n is 5 then
#    *********
#     *******
#      *****
#       ***
#        *
n = int(input('enter the number of rows:--'))
for i in range(0, n):
    for j in range(0, (2*n-1)-(2*i)):
        print('*', end='')
    if i > 0:
        for k in range(0, i):
            print(end=' ')
    print()
    for l1 in range(0, i+1):
        print(end=' ')