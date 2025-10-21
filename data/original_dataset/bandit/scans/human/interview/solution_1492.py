import sys
input = lambda:sys.stdin.readline().rstrip()

h,w=map(int,input().split())
d=w+2
b=[0]*(w+2)
for i in range(h):
  b+=([0]+[int(j=="X") for j in input()]+[0])
b+=([0]*(w+2))
co=sum(b)
t=10**10
for i in range(1,h+1):
  f=0
  for j in range(w+2):
    f+=b[i*d+j]
    if b[i*d+j]==0 and f:
      t=min(t,(f-1)//2)
      f=0
for j in range(1,w+1):
  f=0
  for i in range(h+2):
    f+=b[i*d+j]
    if b[i*d+j]==0 and f:
      t=min(t,(f-1)//2)
      f=0

coo=0
ans=[-1]*(w+2)*(h+2)
stack=[]
for i in range(h+2):
  for j in range(w+2):
    if b[i*d+j]==0:
      stack.append(i*d+j)
      ans[i*d+j]=0
dij=[(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]
for ij in stack:
  i,j=divmod(ij,d)
  for x,y in dij:
    if 0<=i+x<h+2 and 0<=j+y<w+2:
      if ans[(i+x)*d+j+y]==-1:
        ans[(i+x)*d+j+y]=ans[i*d+j]+1
        if ans[(i+x)*d+j+y]>t:
          coo+=1
        stack.append((i+x)*d+(j+y))
if coo*6<co and t==1:
  t-=1
print(t)
for i in range(1,h+1):
  print("".join([".X"[int(t<j)]for j in ans[i*d+1:i*d+w+1]]))