N = 1
while N <= 100:
    count = 0
    i = 2
    while i <= N // 2:
        if N % i == 0:
            count = count + 1
            break
        i = i + 1
    if count == 0 and N > 1:
        print(" %d" % N, end='  ')
    N += 1