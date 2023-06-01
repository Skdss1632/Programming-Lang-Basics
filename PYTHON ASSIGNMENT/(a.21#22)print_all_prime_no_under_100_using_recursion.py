# function to printing_all_prime_no_under_100 using recursion.
def prime(num, i):
    if i == 1:
        print(num, end=' ')
    if num % i == 0:
        if num > 2:
            return prime(num-1, num//2)
    if i > 1:
        return prime(num, i-1)


prime(100, 100 //2)
