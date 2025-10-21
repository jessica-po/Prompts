n = int(input())
INF = 10 ** 18
g = [[INF for i in range(n)] for _ in range(n)]
for i in range(n):
	s = input().rstrip()
	for j in range(n):
		if s[j] == '1':
			g[i][j] = 1
	g[i][i] = 0
for k in range(n):
	for i in range(n):
		for j in range(n):
			g[i][j] = min(g[i][j], g[i][k] + g[k][j])
m = int(input())
p = [int(i) - 1 for i in input().split()]
ptr = 1
ans = [p[0]]
while ptr + 1 < len(p):
	s = ans[-1]
	if g[s][p[ptr]] + 1 != g[s][p[ptr + 1]]:
		ans.append(p[ptr])
	ptr += 1
ans.append(p[-1])
print(len(ans))
for i in ans:
	print(i + 1, end=" ")