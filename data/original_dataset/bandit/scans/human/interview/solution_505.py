import math
from collections import deque

def main():
	n, m, k = list(map(int, input().split()))
	grid = ["" for _ in range(n)]
	x, y = 0, 0

	for i in range(n):
		grid[i] = input()
		if 'X' in grid[i]:
			x, y = i, grid[i].index('X')

	if k % 2 == 1:
		print("IMPOSSIBLE")
		return

	dx = [1, 0, 0, -1]	
	dy = [0, -1, 1, 0]
	names = {(x1, y1): sym for x1, y1, sym in zip(dx, dy, "DLRU")}
	rev_names = {x1: y1 for x1, y1 in zip("DLRU", "URLD")}

	def ok(x, y):
		return (0 <= x < n) and (0 <= y < m) and grid[x][y] != '*'
	

	def bfs(x, y):
		MAX_DIST = (1 << 20)
		dist = [[MAX_DIST for y in range(m)] for x in range(n)]
		dist[x][y] = 0
		q = deque()
		q.append((x, y))

		while len(q) > 0:
			x, y = q.popleft()

			for x0, y0 in zip(dx, dy):
				if ok(x + x0, y + y0) and dist[x][y] + 1 < dist[x + x0][y + y0]:
					dist[x + x0][y + y0] = dist[x][y] + 1
					q.append((x + x0, y + y0))		

		return dist			

	path = []
	x_start, y_start = x, y

	dist = bfs(x_start, y_start)

	for i in range(k // 2):
		for x1, y1 in zip(dx, dy):
			if ok(x + x1, y + y1):
				path.append(names.get((x1, y1)))	
				x += x1
				y += y1
				break
		else:
			print("IMPOSSIBLE")
			return

	moves = k // 2		
	for i in range(k // 2):
		for x1, y1 in zip(dx, dy):
			if ok(x + x1, y + y1) and dist[x + x1][y + y1] <= moves:
				path.append(names.get((x1, y1)))
				x += x1
				y += y1
				moves -= 1
				break

	print("".join(x for x in path))

def __starting_point():
	main()
__starting_point()