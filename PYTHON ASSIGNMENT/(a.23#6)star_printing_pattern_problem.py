# printing star pattern
# if n == 5
# * * * * *
# * * * *
# * * *
# * *
# *
# using for loop
n = int(input('enter a number:-'))
j = n
for i in range(1, n+1):
    j -= 1
    for k in range(1, j+2):
        print('*', end=' ')
    print()
# using while loop
# n = int(input('enter a number:--'))
# i = 1
# while i <= n:
#     j = 1
#     while j <= n-i+1:
#         print('*', end=' ')
#         j += 1
#     print()
#     i += 1
