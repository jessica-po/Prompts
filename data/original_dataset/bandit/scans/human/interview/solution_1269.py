n, m = map(int, input().split())
l = list(map(int, input().split()))
index = [[0 for i in range(n)] for j in range(n)]
for i in range(n):
	mini = 10000000000000
	for j in range(i, n):
		if l[j] < mini:
			inde = j
			mini = l[j]
		index[i][j] = inde
prime = 998244353
d = {}
val = [[1 for i in range(n + 1)] for j in range(n + 1)]
for i in range(n):
	for j in range(n - i):
		if i == 0:
			val[j][j + i] = 1
		elif i == 1:
			val[j][j + i] = 2
		else:
			ind = index[j][j + i]
			sumap = 0
			sumak = 0
			for p in range(j, ind +1):
				sumap += (val[j][p - 1] * val[p][ind - 1]) % prime
			for k in range(ind, j + i + 1):
				sumak += (val[ind + 1][k] * val[k + 1][j + i]) % prime
			val[j][j + i] = (sumap * sumak) % prime
print(val[0][n-1])