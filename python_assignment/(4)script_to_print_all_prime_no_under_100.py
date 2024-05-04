# print all prime number under 100.
N = 1
while N <= 100:
    count = 0
    i = 1
    while i <= N:
        if N % i == 0:
            count += 1
        i = i + 1
    if count == 2 and N > 1:
        print(" %d" % N, end='  ')
    N += 1