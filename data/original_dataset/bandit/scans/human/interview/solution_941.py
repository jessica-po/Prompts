b,k = map(int, input().split())
a = list(map(int, input().split()))
r = 0
for x in a:
	r = (r*b+x) % 2
if r == 0:
	print('even')
else:
	print('odd')