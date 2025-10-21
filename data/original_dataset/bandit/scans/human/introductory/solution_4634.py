for _ in range(int(input())):
	n=int(input())
	s=list(map(int,input().split()))
	l=s.index(1)
	r=n-s[::-1].index(1)
	ans=0
	for i in range(l,r):
		ans+=1-s[i]
	print(ans)