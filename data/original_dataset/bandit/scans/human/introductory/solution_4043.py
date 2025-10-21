n,d,k=list(map(int,input().strip().split()))
ans=[]
if (d>n-1):
	print ("NO")
	return
if (k<2 and n>2):
	print ("NO")
	return
l1=[0 for i in range(d+2)]
count=d
cnt=d+2
def insert(par,v,r,e):
	nonlocal count
	nonlocal cnt
	if count==n-1:
		print ("YES")
		for o in ans:
			print(o[0],o[1])
		return
	else:
		ans.append([par,v])
		cnt=cnt+1
		count=count+1
	if (e==0):
		return 
	while(r!=0):
		insert(v,cnt,k-1,e-1)
		r=r-1
	return 
for i in range(1,d+1):
	ans.append([i,i+1])
for i in range(1,d+2):
	l1[i]=min(i-1,d+1-i)
for i in range(2,d+1):
	r=k-2
	while(r!=0):
		insert(i,cnt,k-1,l1[i]-1)
		r=r-1
if (count<n-1):
	print ("NO")
else:
	print ("YES")
	for o in ans:
		print(o[0],o[1])
	return