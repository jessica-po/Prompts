import math

n=int(input())

def prime(p):
    if p == 1:
        return False
    fl=True
    for i in range(2,math.ceil(p**0.5) + 1):
        if p % i == 0:
            fl=False
    return fl

def sum_of_primes(k):
    fl=True
    for i in range((k // 2) + 1):
        if prime(i) and prime(k-i):
            fl=True
            break
    return fl

if prime(n):
    print(1)
    print(n)
else:
    if prime(n-2):
        print(2)
        print(2 , n-2)
    else:
        l=1
        for i in range(2, (n // 3) + 1):
            if prime(i) and sum_of_primes(n - i):
                l=i
                break
        print(3)
        r=1
        for k in range((n-l) // 2):
            if prime(k) and prime(n-l-k):
                r=k
                break
        print(l,r,n-l-r)