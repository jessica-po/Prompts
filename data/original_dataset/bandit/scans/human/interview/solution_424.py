from math import floor, sqrt
import bisect

import math


def rwh_primes2(n):
    # https://stackoverflow.com/questions/2068372/fastest-way-to-list-all-primes-below-n-in-python/3035188#3035188
    """ Input n>=6, Returns a list of primes, 2 <= p < n """
    correction = (n%6>1)
    n = {0:n,1:n-1,2:n+4,3:n+3,4:n+2,5:n+1}[n%6]
    sieve = [True] * (n//3)
    sieve[0] = False
    for i in range(int(n**0.5)//3+1):
      if sieve[i]:
        k=3*i+1|1
        sieve[      ((k*k)//3)      ::2*k]=[False]*((n//6-(k*k)//6-1)//k+1)
        sieve[(k*k+4*k-2*k*(i&1))//3::2*k]=[False]*((n//6-(k*k+4*k-2*k*(i&1))//6-1)//k+1)
    return [2,3] + [3*i+1|1 for i in range(1,n//3-correction) if sieve[i]]


k = int(input())

primes = rwh_primes2(k)

a = 1
p2 = 2
for i in primes[::-1]:
    if k%i == 0:
        p2 = i
        break

xx = range(k-p2+1, k+1)
#print(list(xx))
if p2>240:
    p1 = primes[bisect.bisect_left(primes, int(math.ceil(xx[0]/2)))]
    print(p1+1)
else:
    ans = k
    p1 = 1
    for x1 in xx:
        for i in primes[::-1]:

            if i >= x1:
                continue

            if x1 % i == 0:
                p1 = i
                break
        ans = min(ans, x1-p1+1)

    print(ans)