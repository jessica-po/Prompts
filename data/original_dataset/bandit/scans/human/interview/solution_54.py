w,m=map(int,input().split())

bb=True

while(m>0 and bb):
	x=m%w
	if x==1:m-=1
	elif x==w-1:m+=1
	elif x!=0:bb=False
	m//=w
	
if bb:print("YES")
else:print("NO")