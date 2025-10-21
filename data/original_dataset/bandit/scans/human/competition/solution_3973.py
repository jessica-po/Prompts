n,m=map(int,input().split())
A=[int(i)-1 for i in input().split()]
ds=[0]*m
de=[[] for i in range(m)]
h,dec=0,0
for i in range(n-1):
  if A[i+1]-A[i]>0:
    h+=A[i+1]-A[i]
  else:
    h+=A[i+1]+1
    dec+=1
  de[A[i+1]].append((i,(A[i+1]-A[i])%m))
for i in range(m):
  for a in de[i]:
    ds[(i-a[1]+1)%m]+=1
ans=float("inf")
for i in range(m):
  for a in de[i]:
    h+=a[1]-1
    dec-=1
  h-=dec
  ans=min(h,ans)
  if i<=m-2:
    dec+=ds[i+1]
  
print(ans)