x0, y0, A, C, B, D = list(map(int, input().split()))

pts = [[x0, y0]]
for i in range(100):
	nx, ny = [pts[-1][0] * A + B, pts[-1][1] * C + D]
	pts.append([nx, ny])
	if max(nx, ny) > 10000000000000000 * 10000000000000000: break


x, y, t = list(map(int, input().split()))
# print (pts[0])
# print (pts[1])
# print (pts[2])
# print (pts[3])
_max = 0
for i in range(len(pts)):
	for j in range(len(pts)):
		if abs(pts[i][0] - pts[j][0]) + abs(pts[i][1] - pts[j][1]) + abs(x - pts[i][0]) + abs(y - pts[i][1]) <= t:
			_max = max(_max, abs(i - j) + 1)
print(_max)