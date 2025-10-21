n = int(input())
a = sorted(list(map(int, input().split())))

ans = 0
for i in range(1, n):
    ans += a[i] - a[i - 1] - 1

print(ans)