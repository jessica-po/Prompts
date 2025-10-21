n = int(input())
xa = []
ya = []
for _ in range(n):
	x, y = map(int,input().split())
	xa.append(x)
	ya.append(y)
print(max(max(xa)-min(xa),max(ya)-min(ya))**2)