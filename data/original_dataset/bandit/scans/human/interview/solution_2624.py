import sys
N, Q = map(int, input().split())
A = list(map(int, input().split()))
Sign = [0]*(3+10**5)
SX = [tuple(sys.stdin.readline().split()) for _ in range(Q)]
mini = 3 + 10**5
Sign = [0]*(3+10**5)
keep = 1
for (s, x) in SX[::-1]:
    x = int(x)
    ax = abs(x) + int((s == '>') ^ (x < 0))
    sin = 1 if s == '<' else -1
    if mini > ax:
        t = sin*keep
        for i in range(mini-1, ax-1, -1):
            Sign[i] = t
        mini = ax
    keep *= (2*(s == '>') - 1) * (2*(0 < x) - 1)
Ans = [None]*N
for i, a in enumerate(A):
    s = Sign[abs(a)]
    if s == 0:
        s = (2*(a > 0) - 1)*keep
    Ans[i] = s*abs(a)
print(*Ans)