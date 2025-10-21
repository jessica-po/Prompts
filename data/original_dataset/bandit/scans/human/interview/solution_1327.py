import sys

N, M = map(int, input().split())

pm = [(i,j,k) for i in range(-1,2,2) for j in range(-1,2,2) for k in range(-1,2,2)]
lst = []

for _ in range(N):
  x,y,z = map(int, input().split())
  lst.append((x,y,z))

rlt = -sys.maxsize
for a,b,c in pm:
  tmp = []
  for x,y,z in lst:
    tmp.append(a*x+b*y+c*z)
  tmp.sort(reverse=True)
  rlt = max(rlt, sum(tmp[:M]))
  
print(rlt)