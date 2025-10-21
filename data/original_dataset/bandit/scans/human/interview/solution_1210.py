n,m=map(int,input().split())
def f():
	a,b=map(int,input().split())
	return(b//m-(a-1)//m)/(b-a+1)
a=[f() for _ in range(n)]
r=0
for i in range(n):
	r+=1-(1-a[i])*(1-a[(i+1)%n])
print(r*2000)