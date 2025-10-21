n,m=map(int,input().split())
if m>n:print(-1)
else:
	q=int((1.+n/m)/2.)
	v=(m+n)/(2*q)
	print(v)