import math
import operator as op

from functools import reduce

from operator import mul    # or mul=lambda x,y:x*y
from fractions import Fraction

def nCk(n,k): 
  return int( reduce(mul, (Fraction(n-i, i+1) for i in range(k)), 1) )


def ncr(n, r):
    r = min(r, n-r)
    if r == 0: return 1
    numer = reduce(op.mul, list(range(n, n-r, -1)))
    denom = reduce(op.mul, list(range(1, r+1)))
    return numer//denom

def modPow(a, x, p):
    #calculates a^x mod p in logarithmic time.
    res = 1
    while(x > 0):
        if( x % 2 != 0):
            res = (res * a) % p
            
        a = (a * a) % p
        x = int(x/2)
    return res

def modInverse(a, p):
    #calculates the modular multiplicative of a mod m.
    #(assuming p is prime).
    return modPow(a, p-2, p)

def modBinomial(n, k, p):
    #calculates C(n,k) mod p (assuming p is prime).

    # n * (n-1) * ... * (n-k+1)
    numerator = 1 
    for i in range(k):
        numerator = (numerator * (n-i) ) % p

    denominator = 1
    for i in range(1, k+1):
        denominator = (denominator * i) % p

    # numerator / denominator mod p.
    return ( numerator* modInverse(denominator,p) ) % p


n, c = input().split()
n = int(n)
c = int(c)

#test = [0 for x in range (n+1)]
#test[1] = c

#for i in range(2, n+1):
#    test[i] = (test[i-1] + modBinomial((i+c-1),i, 1000003))%1000003

#ans = solve(n, c)
#ans =test[n]
ans = modBinomial((c+n),c,1000003) - 1
print(int(ans))