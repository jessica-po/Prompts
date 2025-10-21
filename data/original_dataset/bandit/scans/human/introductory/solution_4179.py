n,m,c=map(int,input().split())
b=list(map(int,input().split()))
r=0
for _ in range(n):
  a=list(map(int,input().split()))
  d=0
  for jj in range(m):
    d+=a[jj]*b[jj]
  if d+c>0:
    r+=1
print(r)