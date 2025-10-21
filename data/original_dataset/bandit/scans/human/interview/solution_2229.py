import sys
import math

def sieve(n):
    prime_factors = [[] for i in range(n+1)]
    tmp = [True] * (n+1)
    tmp[0] = tmp[1] = False
    for i in range(2, n+1):
        if tmp[i]:
            for k in range(i, n+1, i):
                tmp[k] = False
                prime_factors[k].append(i)
    return prime_factors

n = int(sys.stdin.readline().strip())
a = list(map(int, sys.stdin.readline().strip().split(' ')))
b = []
forbidden_factors = set({})
prime_factors = sieve(2000005)
is_greater = False
min_available = 2

for ai in a:
    factors = prime_factors[ai]
    if not is_greater:
        curr = ai
        ok = True
        for f in factors:
            if f in forbidden_factors:
                ok = False
                break
        if ok:
            for f in factors:
                forbidden_factors.add(f)
        else:
            is_greater = True
            ok = False
            while not ok:
                curr += 1
                ok = True
                factors = prime_factors[curr]
                for f in factors:
                    if f in forbidden_factors:
                        ok = False
                        break
            for f in factors:
                forbidden_factors.add(f) 
    else:
        curr = min_available
        ok = True
        factors = prime_factors[curr]
        for f in factors:
            if f in forbidden_factors:
                ok = False
                break
        while not ok:
            curr += 1
            ok = True
            factors = prime_factors[curr]
            for f in factors:
                if f in forbidden_factors:
                    ok = False
                    break
        min_available = curr
        for f in factors:
            forbidden_factors.add(f)
    b.append(str(curr))
print(" ".join(b))