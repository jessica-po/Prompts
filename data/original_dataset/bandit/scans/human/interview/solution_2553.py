q = int(input())
for ii in range(q):
	n,x = map(int,input().split())
	l = list(map(int,input().split()))
	par = 0
	npar = 0
	for i in l:
		if i%2 == 1:
			npar += 1
		else:
			par += 1
	if x == n:
		if npar%2 == 1:
			print("Yes")
		else:
			print("No")
	else:
		if npar > 0 and par > 0:
			print("Yes")
		else:
			if par == 0:
				if x%2 == 1:
					print("Yes")
				else:
					print("No")
			else:
				print("No")