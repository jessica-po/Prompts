n=int(input())
a=list(int(i) for i in input().split())
p=[0]*(n+1)
for i in range(0,n) :
	p[i+1]+=p[i]+a[i]
ok=dict()
ans,l=0,0
for i in range(n+1) :
	if p[i] in ok :
		ok[p[i]]+=1
	else :
		ok[p[i]]=1
	while ok[p[i]]>1:
		ok[p[l]]-=1
		l+=1
	ans+=(i-l+1)
print(ans-n-1)