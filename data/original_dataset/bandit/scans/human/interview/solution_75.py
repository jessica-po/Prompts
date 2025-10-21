n, m = list(map(int, input().split()))
p = []
ans = 0
for i in range(n):
    s = input()
    ans += s.count('*')
    p.append(s)
dp = []
for i in range(n):
    dp.append([0] * m)
for i in range(n):
    col = p[i].count('*')
    for t in range(m):
        dp[i][t] = col
for i in range(m):
    col = 0
    for t in range(n):
        if p[t][i] == '*':
            col += 1
    for t in range(n):
        dp[t][i] += col
f = False
for i in range(n):
    for t in range(m):
        if dp[i][t] - int(p[i][t] == '*') == ans:
            f = True
            print('YES')
            print(i + 1, t + 1)
            break
    if f:
        break
if not f:
    print('NO')