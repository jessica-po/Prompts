read_line = lambda: [int(i) for i in input().split()]

n, m, k = read_line()
a = [read_line() for i in range(n)]
if n < m:
    n, m, a = m, n, list(zip(*a))

xs = []
for y in a:
    x = 0
    for b in y:
        x = 2 * x + b
    xs.append(x)

def work(y):
    tot = 0
    for x in xs:
        c = bin(x ^ y).count('1')
        tot += min(c, m - c)
    return tot

ans = min(list(map(work, xs if m > k else list(range(1<<m)))))

print(ans if ans <= k else -1)