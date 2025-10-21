x, y = map(int, input().split())

if y == 0:
	print('No')
	return
else:
	y -= 1

if y == 0 and x:
	print('No')
	return

if y > x or (x - y) & 1:
	print('No')
else:
	print('Yes')