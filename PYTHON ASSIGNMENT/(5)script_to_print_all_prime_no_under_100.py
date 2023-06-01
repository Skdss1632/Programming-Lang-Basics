for N in range(1, 101):
    count = 0
    for i in range(1, N + 1):
        if N % i == 0:
            count += 1
    if count == 2 and N > 1:
        print(" %d" % N, end=' ')
