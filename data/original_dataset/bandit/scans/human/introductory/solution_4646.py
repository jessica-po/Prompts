for _ in range(int(input())):
	n=int(input())
	a=list(map(int,input().split()))

	od=0
	ev=0

	for i in range(n):
		if(i&1):
			if(a[i]%2==0):
				od+=1
		else:
			if(a[i]&1):
				ev+=1

	if(od!=ev):
		print(-1)
	else:
		print(od)