n, m = list(map(int, input().split()))
M = [list(map(int, input().split())) for r in range(n)]

depth = [[1] * m for r in range(n)]

for c in range(m):
    for r in range(1, n):
        if M[r][c] >= M[r - 1][c]:
            depth[r][c] = depth[r - 1][c] + 1

max_depth = [max(col) for col in depth]

ans = ""
k = int(input())
for i in range(k):
    l, r = list(map(int, input().split()))
    if max_depth[r - 1] >= r - l + 1:
        ans += "Yes\n"
    else:
        ans += "No\n"

print(ans)