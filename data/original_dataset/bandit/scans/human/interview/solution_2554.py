def subsolve(a):
    c = 0
    m = 0
    for i in a:
        c += i
        if c < 0:
            c = 0
        m = max(m, c)
    return m
def solve():
    n = int(input())
    a = list(map(int, input().split()))
    s = 0
    for i in range(0, n, 2):
        s += a[i]
    u = subsolve([a[i] - a[i - 1] for i in range(1, n, 2)])
    v = subsolve([a[i - 1] - a[i] for i in range(2, n, 2)])
    print(max(u, v) + s)
t = int(input())
for _ in range(t):
    solve()