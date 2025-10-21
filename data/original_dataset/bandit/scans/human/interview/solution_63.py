n,k=map(int,input().split())
l=list(map(int,input().split()))
pf=[]
needed=[]
for i in range(2,40000):
	if k%i==0:
		pf.append(i)
		c=0
		while k%i==0:
			k//=i
			c+=1
		needed.append(c)
if k>1:
	pf.append(k)
	needed.append(1)
pfl=len(pf)
cnt=[[0]*n for i in range(pfl)]
for i in range(n):
	for j in range(len(pf)):
		c=0
		while l[i]%pf[j]==0:
			c+=1
			l[i]//=pf[j]
		cnt[j][i]=c
have=[sum(i) for i in cnt]
pos=n
def ok():
	for i in range(len(pf)):
		if have[i]<needed[i]:
			return False
	return True
if not ok():
	print(0)
	quit()
for i in range(n-1,0,-1):
	for j in range(len(pf)):
		have[j]-=cnt[j][i]
	if not ok():
		for j in range(len(pf)):
			have[j]+=cnt[j][i]
		break
	pos=i
ans=n-pos+1
for x in range(n-1):
	for j in range(len(pf)):
		have[j]-=cnt[j][x]
	if pos==(x+1):
		for j in range(len(pf)):
			have[j]+=cnt[j][pos]
		pos+=1
	while pos<n:
		if ok():
			break
		else:
			for i in range(len(pf)):
				have[i]+=cnt[i][pos]
			pos+=1
	if ok():
		ans+=n-pos+1
	else:
		break
print(ans)