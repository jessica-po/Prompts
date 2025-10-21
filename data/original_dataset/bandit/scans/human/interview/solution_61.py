n, bx = list(map(int, input().split()))
x1 = list(map(int, input().split()))
x = 0
for i in range(n):
	x *= bx
	x += x1[i]

n, by = list(map(int, input().split()))
y1 = list(map(int, input().split()))
y = 0
for i in range(n):
	y *= by
	y += y1[i]

if x == y:
	print('=')
elif x < y:
	print('<')
else:
	print('>')