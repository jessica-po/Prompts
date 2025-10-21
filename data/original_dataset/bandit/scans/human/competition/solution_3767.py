f = lambda: list(map(int, input().split()))
n = int(input())
a, b = f(), f()

d = [[None] * 10001 for i in range(n)]

def g(i, s):
    if s <= 0: return (0, s)
    if i == n: return (1e7, 0)

    if not d[i][s]:
        x, y = g(i + 1, s - b[i])
        d[i][s] = min(g(i + 1, s), (x + 1, y + b[i] - a[i]))
    return d[i][s]

x, y = g(0, sum(a))
print(x, y)