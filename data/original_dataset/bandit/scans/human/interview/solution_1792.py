import sys

def matching(node, visited, adj, assigned):
	if node == -1:
		return True
	if visited[node]:
		return False
	visited[node] = True
	for neighbor in adj[node]:
		if matching(assigned[neighbor], visited, adj, assigned):
			assigned[neighbor] = node
			return True
	return False

INF = 1000 * 1000

inp = [int(x) for x in sys.stdin.read().split()]

n, m = inp[0], inp[1]
inp_idx = 2

G = [[INF] * n for _ in range(n)]

for _ in range(m):
	a, b = inp[inp_idx] - 1, inp[inp_idx + 1] - 1
	inp_idx += 2
	G[a][b] = G[b][a] = 1

for v in range(n):
	G[v][v] = 0
	
for k in range(n): 
	for i in range(n): 
		for j in range(n): 
			G[i][j] = min(G[i][j], G[i][k] + G[k][j])
	
s, b, k, h = inp[inp_idx], inp[inp_idx + 1], inp[inp_idx + 2], inp[inp_idx + 3]
inp_idx += 4

spaceships = []
for _ in range(s):
	x, a, f = inp[inp_idx] - 1, inp[inp_idx + 1], inp[inp_idx + 2]
	inp_idx += 3
	spaceships.append((x, a, f))
	
bases = []
for _ in range(b):
	x, d = inp[inp_idx] - 1, inp[inp_idx + 1]
	inp_idx += 2
	bases.append((x, d))
	
adj = [[] for _ in range(s)]
assigned = [[] for _ in range(b)]
for i in range(s):
	space = spaceships[i]
	for j in range(b):
		base = bases[j]
		u, v = space[0], base[0]
		fuel = space[2]
		if G[u][v] <= fuel and space[1] >= base[1]:
			adj[i].append(j)

visited = [False] * s
assigned = [-1] * b

matched = 0
for i in range(s):
	visited = [False] * s
	if matching(i, visited, adj, assigned):
		matched += 1


print(min(matched * k, h * s))