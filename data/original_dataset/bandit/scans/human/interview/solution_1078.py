n = int(input())
z = 0
for i in range(n):
	x = int(input())
	if x % 2 == 0:
		print(x//2)
	else:
		if z == 1:
			print((x-1)//2)
		else:
			print((x+1)//2)
		z = 1 - z