import sys

mod = 10**9 + 7

def solve():
    n = int(input())
    a = [int(i) for i in input().split()]

    cnt = [0]*(10**5 + 1)

    for ai in a:
        for d in range(1, ai + 1):
            if d*d > ai:
                break
            if ai % d == 0:
                if d != ai // d:
                    cnt[d] += 1
                    cnt[ai // d] += 1
                else:
                    cnt[d] += 1

    ans = 0

    for i in range(1, 10**5 + 1):
        ans += mobius(i) * (pow(2, cnt[i], mod) - 1)
        ans %= mod

    print(ans)

def mobius(x):
    assert x >= 1

    divcnt = 0

    for p in range(2, x + 1):
        if p*p > x:
            break
        if x % p != 0:
            continue

        x //= p

        if x % p == 0:
            return 0
        else:
            divcnt ^= 1

    if x > 1:
        divcnt ^= 1

    return (-1)**divcnt

def __starting_point():
    solve()
__starting_point()