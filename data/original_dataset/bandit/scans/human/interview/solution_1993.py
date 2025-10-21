"""
	Author		: Arif Ahmad
	Date  		: 
	Algo  		: 
	Difficulty	: 
"""
from sys import stdin, stdout
from collections import deque

g = None # contains the actual graph
h = None # h[x][y] represents the component in which cell (x,y) belongs
r = None
c = None
visited = None
total = None
comp = None
dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]


def bfs(x, y):
	nonlocal total
	
	q = deque([(x, y)])
	total += 1
	visited[x][y] = True
	h[x][y] = comp
	while q:
		x, y = q.pop()
		#print('comp:', comp, 'cell:', x, y)
		for k in range(4):
			#print('loop:', k)
			nx = x + dx[k]
			ny = y + dy[k]
			#print(visited)
			#print('new cell:', nx, ny, 'check:', nx>=0 , nx<r , ny>=0 , ny<c , visited[nx][ny]==False , g[nx][ny]=='.')
			if nx>=0 and nx<r and ny>=0 and ny<c and visited[nx][ny]==False and g[nx][ny]=='.':
				q.appendleft((nx, ny))
				total += 1
				visited[nx][ny] = True
				h[nx][ny] = comp


def main():
	nonlocal g, h, r, c, visited, comp, total

	r, c = [int(_) for _ in stdin.readline().split()]

	g = []
	for i in range(r):
		line = stdin.readline()
		g.append(list(line))

	component = []
	h = [[-1 for i in range(c)] for j in range(r)]
	visited = [[False for i in range(c)] for j in range(r)]
	#print(visited)

	for i in range(r):
		for j in range(c):
			if visited[i][j] == False and g[i][j] == '.':
				comp = len(component)
				total = 0
				#print('calling bfs', i, j)
				bfs(i, j)
				component.append(total)

	for x in range(r):
		for y in range(c):
			if g[x][y] == '*':
				ans = 0
				idx = set()
				for k in range(4):
					nx = x + dx[k]
					ny = y + dy[k]
					if nx>=0 and nx<r and ny>=0 and ny<c and g[nx][ny]=='.':
						idx.add(h[nx][ny])
				for item in idx:
					#print(component[item])
					ans += component[item]
				ans += 1
				ans %= 10
				g[x][y] = str(ans)

	#print(component)
	for i in range(r):
		stdout.write(''.join(g[i]))

	

def __starting_point():
    main()

__starting_point()