n = int(input())
points = [[int(x) for x in input().split()] for _ in range(n)]
if n <= 1:
	print(-1)
	return
dx = [1e9, -1e9]
dy = [1e9, -1e9]
for x, y in points:
	dx[0] = min(dx[0], x)
	dx[1] = max(dx[1], x)
	dy[0] = min(dy[0], y)
	dy[1] = max(dy[1], y)
area = (dx[1] - dx[0]) * (dy[1] - dy[0])
if area:
	print(area)
else:
	print(-1)