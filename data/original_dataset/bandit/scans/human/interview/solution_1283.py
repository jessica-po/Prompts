import sys
import math

n, k = list(map(int,sys.stdin.readline().strip().split(' ')))
grid = []
for n0 in range(n):
	grid.append([char for char in sys.stdin.readline().strip()])

res = [[0 for i in range(n)] for j in range(n)]

for i in range(n):
	for j in range(n):
		if grid[i][j] == '#':
			continue
		ii, jj = i,j

		cpt = 0
		while ii < n and cpt < k:
			if grid[ii][j] == '#':
				break
			else:
				cpt += 1
			ii += 1
		if cpt == k:
			for ii in range(i,i+k):
				res[ii][j] += 1

		cpt = 0
		while jj < n and cpt < k:
			if grid[i][jj] == '#':
				break
			else:
				cpt += 1
			jj += 1
		if cpt == k:
			for jj in range(j,j+k):
				res[i][jj] += 1
ans = [0,0]
maxsf = -1
for i in range(n):
	for j in range(n):
		if res[i][j] > maxsf:
			ans = [i,j]
			maxsf = res[i][j]
print(ans[0]+1, ans[1]+1)