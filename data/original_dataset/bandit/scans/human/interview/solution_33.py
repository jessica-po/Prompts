import sys, collections

def gcd(a, b):
    if b == 0: return a
    return gcd(b, a % b)

def lcm(a, b):
    return a // gcd(a, b) * b

def extgcd(a, b):
    if b == 0: return 1, 0
    x, y = extgcd(b, a % b)
    return y, x - a // b * y

def prime_factor(n):
    res = collections.defaultdict(int)

    i = 2
    while i * i <= n:
        cnt = 0
        while n % i == 0:
            n //= i
            cnt += 1
        if cnt > 0: res[i] = cnt
        i += 1
    if n != 1: res[n] = 1

    return res

def modinv(a, mod):
    if a == 0: return -1
    if gcd(a, mod) != 1: return -1
    return extgcd(a, mod)[0] % mod

def normalize(a1, a2):
    p1 = prime_factor(a1)
    p2 = prime_factor(a2)

    keys = list(set(p1.keys()) | set(p2.keys()))

    r1 = 1
    r2 = 1
    for k in keys:
        if p1[k] >= p2[k]:
            r1 *= k ** p1[k]
        else:
            r2 *= k ** p2[k]
    return r1, r2

def solve(a1, b1, a2, b2):
    g = gcd(a1, a2)
    if (b1 - b2) % g != 0: return -1

    a1, a2 = normalize(a1, a2)
    u = b1 % a1
    inv = modinv(a1, a2)
    v = (b2 - u) * inv % a2
    return u + v * a1

def f(x0, T, v):
    ok = 10 ** 36
    ng = -1

    while ok - ng > 1:
        mid = (ok + ng) // 2

        if x0 + T * mid >= v:
            ok = mid
        else:
            ng = mid

    return ok

a1, b1, a2, b2, L, R = map(int, input().split())

T = lcm(a1, a2)
x0 = solve(a1, b1, a2, b2)

if x0 == -1:
    print(0)
    return

x0 -= T * 10 ** 36

ok = 10 ** 60
ng = -1

while ok - ng > 1:
    mid = (ok + ng) // 2

    val = x0 + T * mid
    k = (val - b1) // a1
    l = (val - b2) // a2
    if k >= 0 and l >= 0:
        ok = mid
    else:
        ng = mid

x0 += ok * T

# L <= x0 + kT < R + 1
ans = f(x0, T, R + 1) - f(x0, T, L)

print(ans)