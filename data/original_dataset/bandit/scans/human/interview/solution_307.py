k2, k3, k5, k6 = list(map(int, input().split()))
c = min(k2, k5, k6)
k2 -= c
ans = 256 * c
ans += 32 * min(k3, k2)
print(ans)