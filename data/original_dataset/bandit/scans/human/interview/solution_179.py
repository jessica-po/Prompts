MOD = 1000000007


def f(n, cnt):
    """
    n! / (n - cnt)!
    """
    ans = 1
    for _ in range(cnt):
        ans = (ans * n) % MOD
        n -= 1
    return ans


def main():
    n, x, pos = list(map(int, input().split()))
    chk1 = 0
    chk_r = 0
    left = 0
    right = n
    while left < right:
        middle = (left + right) // 2
        if middle <= pos:
            if middle < pos:
                chk1 += 1
            left = middle + 1
        else:
            chk_r += 1
            right = middle
    if chk1 > x - 1 or chk_r > n - x:
        print(0)
    else:
        # (x - 1)! / (x - 1 - chk1)! * (n - x)! / (n - x - chk_r)! * (n - chk1 - chk_r - 1)!
        rest = n - chk1 - chk_r - 1
        print(f(x - 1, chk1) * f(n - x, chk_r) * f(rest, rest) % MOD)


main()