'''input
3 3
>>>
<<<
>>>
'''
#print(input().split())
n, m = list(map(int, input().split()))
#return
g = []
for i in range(n):
	g += [input()]
# print(g)


memo = {}

def dfs(u):
	if u not in memo:
		memo[u] = res = 1
		if u < n:
			for v in range(m):
				if g[u][v] == '>':
					res = max(res, dfs(n + v) + 1)
			for v in range(m):
				if g[u][v] == '=':
					res = max(res, dfs(n + v))
			for v in range(m):
				if g[u][v] == '=':
					memo[n + v] = max(memo[n + v], res)
		else:
			for v in range(n):
				if g[v][u - n] == '<':
					res = max(res, dfs(v) + 1)
			for v in range(n):
				if g[v][u - n] == '=':
					res = max(res, dfs(v))
			for v in range(n):
				if g[v][u - n] == '=':
					memo[v] = max(memo[v], res)
		memo[u] = res
	return memo[u]
ans = [0] * (n + m)
for i in range(n + m):
	ans[i] = dfs(i)
for i in range(n):
	for j in range(m):
		if g[i][j] == '=' and ans[i] != ans[n + j]:
			print("No")
			return
		if g[i][j] == '<' and ans[i] >= ans[n + j]:
			print("No")
			return
		if g[i][j] == '>' and ans[i] <= ans[n + j]:
			print("No")
			return
print("Yes")
print(*ans[:n])
print(*ans[n:])