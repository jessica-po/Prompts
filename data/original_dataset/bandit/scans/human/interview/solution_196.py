x, k = map(int, input().split())
if x == 0:
    print(0)
else:
    mod = 10 ** 9 + 7
    p = pow(2, k, mod)
    ans = (x * (p * 2) - (p - 1)) % mod
    print(ans)