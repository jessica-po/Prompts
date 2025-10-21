import sys
import math

def factorization(n):
    res = []
    limit = math.ceil(math.sqrt(n))
    p = 2
    cnt = 0

    while n % p == 0:
        cnt += 1
        n //= p

    if cnt > 0:
        res.append((p, cnt))

    cnt = 0
    for p in range(3, limit + 1, 2):
        if n % p == 0:
            while n % p == 0:
                cnt += 1
                n //= p

            res.append((p, cnt))
        cnt = 0

    if n > 1:
        res.append((n, 1))

    return res

def divisor(n):
    res = set()

    factor = factorization(n)

    for p, c in factor:
        if res == set():
            for i in range(c + 1):
                res.add(p ** i)
        else:
            t = set()
            for i in range(1, c + 1):
                for m in res:
                    t.add(m * p**i)
            res = res | t

    res = list(sorted(res))
    return res

n, k = map(int, input().split())

# print(factorization(n), file=sys.stderr)
# print(divisor(n), file=sys.stderr)

n_div = divisor(n)

if n == 1:
    if k == 1:
        ans = 1
    else:
        ans = -1
elif k > len(n_div):
    ans = -1
else:
    ans = n_div[k - 1]

print(ans)