n = int(input())
a = list(map(int, input().split()))
maxi = 0
ans = 0
for i in range(n):
    a[i] -= 1
    maxi = max(maxi, a[i])
    if maxi == i:
        ans += 1
print(ans)