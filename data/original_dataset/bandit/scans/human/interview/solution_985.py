a=[0]*2222
b=[0]*2222
r=0
for _ in range(int(input())):
	x,y=map(int,input().split())
	r+=a[x+y]+b[x-y+1111]
	a[x+y]+=1
	b[x-y+1111]+=1
print(r)