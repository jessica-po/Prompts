t = int(input())
for tt in range(t):
	x, y = map(int, input().split())
	print('YES' if x % y == 0 else "NO")