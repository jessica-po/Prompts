m = int(input())
c = list(map(int,input().split()))
x, y = list(map(int,input().split()))

for i in range(m):
	sb = sum(c[:-i-1])
	si = sum(c[-i-1:])
	if x <= sb <= y:
		if x <= si <= y:
			print(m-i)
			break
else:
	print(0)