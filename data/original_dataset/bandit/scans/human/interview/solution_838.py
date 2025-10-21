read = lambda: map(int, input().split())
n, m = read()
a = [list(read()) for i in range(n)]
ans = n * m
for i in range(n):
    cnt0 = a[i].count(0)
    cnt1 = a[i].count(1)
    if cnt0 > 1: ans += (2 ** cnt0 - cnt0 - 1)
    if cnt1 > 1: ans += (2 ** cnt1 - cnt1 - 1)
for i in range(m):
    cnt0 = sum(a[j][i] == 0 for j in range(n))
    cnt1 = sum(a[j][i] == 1 for j in range(n))
    if cnt0 > 1: ans += (2 ** cnt0 - cnt0 - 1)
    if cnt1 > 1: ans += (2 ** cnt1 - cnt1 - 1)
print(ans)