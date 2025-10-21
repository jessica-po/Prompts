import os
from io import BytesIO

# input = BytesIO(os.read(0, os.fstat(0).st_size)).readline


def check(x, p):
    i = x - 1
    while i > -1 and a[i] <= p:
        p -= a[i]
        if i >= k - 1:
            i -= k
        else:
            i -= 1
    return i <= -1


for _ in range(int(input())):
    n, p, k = map(int, input().split())
    a = sorted(map(int, input().split()))
    dp = [1000000000] * (n + 1)
    dp[0] = 0
    ans = 0
    for i in range(1, n + 1):
        dp[i] = dp[i - 1] + a[i - 1]
        if i - k + 1 >= 0:
            dp[i] = min(dp[i], dp[i - k] + a[i - 1])
        if dp[i] <= p:
            ans = i
    print(ans)