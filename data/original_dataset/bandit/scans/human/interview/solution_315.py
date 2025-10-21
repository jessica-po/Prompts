n, k = list(map(int, input().split()))
a = list(map(int, input().split()))

ans = 0
for i in range(1, n):
    diff = k - (a[i] + a[i - 1])
    if diff > 0:
        a[i] += diff
        ans += diff

print(ans)
print(' '.join(map(str, a)))