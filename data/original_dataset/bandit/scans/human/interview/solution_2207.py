n, m = map(int, input().split())
a = [input() for i in range(n)]
ans = 0
i = 0
while i < m:
    if a[n-1][i] == "B":
        ans += 1
        while i < m and a[n-1][i] == "B":
            i += 1
    i += 1

print(ans)