a, b = input().split(' ')
n = int(input())

d = {'v': 0, '>': 1, '^': 2, '<': 3}

a, b = d[a], d[b]

ccw = bool((a + n) % 4 == b)
cw = bool((a - n) % 4 == b)

if cw and not ccw:
	print('cw')
elif ccw and not cw:
	print('ccw')
else:
	print('undefined')