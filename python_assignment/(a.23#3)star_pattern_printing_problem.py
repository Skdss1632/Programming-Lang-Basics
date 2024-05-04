# star pattern printing
# if n is 5 then
#     *
#    ***
#   *****
#  *******
# *********
n = int(input('enter the number of rows:--'))
for i in range(0, n):
    for j in range(1, 2*n):
        print(end=' ')
        if j == n - i:
            for k in range(1, 2*i+2):
                print('*', end='')
    print()

# 2nd approach
# n = int(input('enter a no:--'))
# for i in range(0, n):
#     for j in range(1, n-i):
#         print(' ', end='')
#     for k in range(1, (2*i+1)+1):
#         print('*', end='')
#     for l1 in range(1, n-i):
#         print(' ', end='')
#     print()