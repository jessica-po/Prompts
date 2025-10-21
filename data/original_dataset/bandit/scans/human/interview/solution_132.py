n = int(input())
a = list(map(int, input().split()))
mn = 360
for i in range(n):
    x = 0
    for j in range(i, n):
        x += a[j]
        mn = min(mn, abs(x - (360 - x)))
print(mn)