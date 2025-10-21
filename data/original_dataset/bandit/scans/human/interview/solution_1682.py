read = lambda: map(int, input().split())
n, k = read()
a = list(read())
b = list(read())
c = [(a[i], b[i]) for i in range(n)]
c.sort(key = lambda x: x[0] - x[1])
ans = sum(c[i][0] for i in range(k))
for i in range(k, n):
    ans += min(c[i][0], c[i][1])
print(ans)