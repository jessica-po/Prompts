n,k=map(int,input().split())
a=list(input())
ans,cnt=list(list()),0
while True :
	cur=list()
	for i in range(n-1) :
		if a[i]=='R' and a[i+1]=='L' :
			cur.append(i)
			cnt+=1
	if len(cur)>0:
		ans.append(cur.copy())
		for i in cur :
			a[i],a[i+1]=a[i+1],a[i]
	else :
		break 
if len(ans)>k or cnt<k:
	print(-1)
else :
	lst=list()
	dumb=k-len(ans)
	w,p=0,0
	while dumb>0 :
		lst.append("1 "+str(ans[w][p]+1)+"\n")
		dumb-=1
		p+=1
		if p==len(ans[w]) :
			p=0
			w+=1
			dumb+=1
	while w<len(ans) :
		lst.append(str(len(ans[w])-p)+" ")
		while p<len(ans[w]) :
			lst.append(str(ans[w][p]+1)+" ")
			p+=1
		lst.append("\n")
		w+=1
		p=0
	print("".join(lst))