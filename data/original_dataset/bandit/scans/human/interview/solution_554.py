n, m = list(map(int, input().split()))
a = [0] + list(map(int, input().split()))
pr = [0 for i in range(len(a))]
for i in range(1, len(a)):
    pr[i] = pr[i - 1] + a[i]

ans = 0
for i in range(m):
    l, r = list(map(int, input().split()))
    cur = pr[r] - pr[l - 1]
    if cur >= 0:
        ans += cur

print(ans)