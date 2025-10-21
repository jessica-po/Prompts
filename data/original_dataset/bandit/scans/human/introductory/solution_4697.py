n, m = [int(x) for x in input().split()]
ans = min(n, m // 2)
ans += (m - ans * 2) // 4
print(ans)