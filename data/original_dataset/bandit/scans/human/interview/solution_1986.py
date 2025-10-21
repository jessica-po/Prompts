import sys

(n, k) = [int(x) for x in sys.stdin.readline().strip().split()]

ans = -999999999999999999999999999999999999999999

for i in range(0, n):
    (f, t) = [int(x) for x in sys.stdin.readline().strip().split()]
    ans = max(ans, f-max(0,t-k))

print(ans)