from math import sqrt, log2
from sys import stdin
from bisect import bisect
import time

def all_primes(n):
    res = []
    for i in range(1, n+1):
        prime = True
        for j in range(2, min(int(sqrt(i))+2, i)):
            if i % j == 0:
                prime = False
                break
        if prime: res.append(i)
    return res


def count_pow_nums(n, p):  #don't count 1
    top = int(pow(n, 1.0/p))
    if pow(top+2, p) <= n:
        return top+1
    elif pow(top+1, p) <= n:
        return top
    elif pow(top, p) <= n:
        return top-1
    else:
        return top-2
primes = all_primes(64)
num_set=set()
max_n = 1000000000000000000
for pi in range(3, len(primes)):
    p = primes[pi]
    cnt = count_pow_nums(max_n, p)
    for n in range(2, cnt+5):
        sq2 = round(sqrt(n))
        sq3 = round(pow(n, 1/3))
        if sq2**2 != n and sq3**3 != n:
            num = pow(n, p)
            if num <= max_n:
                num_set.add(num)
nums = sorted(num_set)
t = int(stdin.readline())
for i in range(t):
    n = int(stdin.readline())
    ans = n-1-count_pow_nums(n, 2)-count_pow_nums(n, 3)+count_pow_nums(n, 6)
    ans -= bisect(nums, n)
    print(ans)