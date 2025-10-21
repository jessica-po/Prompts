import os
import sys

if os.getenv("LOCAL"):
    sys.stdin = open("_in.txt", "r")

sys.setrecursionlimit(2147483647)
INF = float("inf")

N = int(sys.stdin.readline())
S = list(map(int, sys.stdin.readline().split()))


def count_max(diff):
    # 左右対称に diff 間隔でとるときの最大
    b = 0
    a = N - 1
    ret = 0
    cumsum = 0
    while diff < a and a != b and b - a != diff:
        cumsum += S[b] + S[a]
        ret = max(ret, cumsum)
        b += diff
        a -= diff
    return ret


ans = 0
for diff in range(1, N // 2 + 1):
    ans = max(ans, count_max(diff))
print(ans)