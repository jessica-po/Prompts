n,k = list(map(int,input().split()))
if n > 2:
	if k == n:
		print("-1")
	elif k < n-1:
		p = [n]
		for i in range(2,k+2):
			p.append(i)
		p.append(1)
		for i in range(k+2,n):
			p.append(i)
		print(*p)
	elif k == n-1:
		p = []
		for i in range(1,n+1):
			p.append(i)
		print(*p)
		
elif n == 2:
	if k == 1:
		print("1 2")
	elif k == 0:
		print("2 1")
	else:
		print("-1")
else:
	if k == 0:
		print("1")
	else:
		print("-1")