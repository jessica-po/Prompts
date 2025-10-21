n, s = list(map(int, input().split()))
a = list(map(int, input().split()))

total = sum(a)

ans = []
for i in range(n):
    high = s - (total - a[i])
    low = s - (n - 1)
    
    cur = 0
    if low <= a[i]:
        cur += a[i] - low
    if high > 0:
        cur += high - 1

    ans.append(cur)

print(' '.join(map(str, ans)))