# diamond star pattern
# if n == 3 then
#           *
#          ***
#         *****
#         *****
#          ***
#           *

n = int(input('enter a no:--'))
for i in range(0, n):
    for j in range(1, n-i):
        print(' ', end='')
    for k in range(1, (2*i+1)+1):
        print('*', end='')
    for l1 in range(1, n-i):
        print(' ', end='')
    print()
for i in range(0, n):
    for j in range(0, (2 * n - 1) - (2 * i)):
        print('*', end='')
    if i > 0:
        for k in range(0, i):
            print(end=' ')
    print()
    for l1 in range(0, i + 1):
        print(end=' ')