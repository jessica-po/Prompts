n = int(input())
vlst = list(map(int, input().split()))
clst = list(map(int, input().split()))
ans = 0
for v, c in zip(vlst, clst):
    ans += max(0, v - c)
print(ans)