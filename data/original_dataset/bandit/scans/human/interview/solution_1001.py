n = int(input())
a = [0] * n
a = list(map(int, input().split()))
for i in range(1, len(a)):
    a[i] += a[i - 1]

ans = a[-1]
for i in range(n - 2, 0, -1):
    ans = max(ans, a[i] - ans)
print(ans)