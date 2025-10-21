def f(n, mod):
    res = 0
    n1 = 1
    n2 = 2
    k = 1
    now = 0
    while n >= k:
        if now == 0:
            now = 1
            res = (res + n1 * k + (k * (k - 1))) % mod
            n -= k
            k *= 2
            n1 = n1 + k
        else:
            now = 0
            res = (res + n2 * k + (k * (k - 1))) % mod
            n -= k
            k *= 2
            n2 = n2 + k
    if n == 0:
        return res
    if now == 0:
        return (res + n1 * n + (n * (n - 1))) % mod
    return (res + n2 * n + (n * (n - 1))) % mod

l, r = list(map(int, input().split()))
mod = 10 ** 9 + 7
print((f(r, mod) - f(l - 1, mod)) % mod)