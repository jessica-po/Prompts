import collections

N=int(input())
L=list(map(int,input().split()))
L=sorted(L)
C=collections.Counter(L)
D=list(C.keys())
E=list(C.values())
K=len(C)
ans=0
for i in range(K):
	if D[i]==E[i]:
		ans+=0
	if D[i]>E[i]:
		ans+=E[i]
	if D[i]<E[i]:
		ans+=(E[i]-D[i])
print(ans)