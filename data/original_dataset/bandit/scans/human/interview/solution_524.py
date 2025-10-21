n=int(input())
a=list(map(int,input().split()))
a=sorted(a)

if(n>65):
	print(sum(a)-n)
elif(n==1 or n==2):
	print(a[0]-1)
else:
	ans=10**20

	for i in range(1,50000):
		now=1
		ta=0
		for j in a:
			ta+=abs(now-j)
			now*=i
		ans=min(ans,ta)

	print(ans)