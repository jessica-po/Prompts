n=int(input())
d={}
d1={}
for i in range(n):
  a,b=list(map(int,input().split()))
  d[a]=b
  d1[b]=a
r=[0]*n
front=0
i=1
while i<n:
  r[i] = d.get(front)
  front = r[i]
  i += 2
for f in list(d.keys()):
  if d1.get(f) == None:
    front = f
    break
r[0]=front
i=2
while i<n:
  r[i] = d.get(front)
  front = r[i]
  i += 2
print(*r)