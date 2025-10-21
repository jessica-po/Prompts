M,S=list(map(int,input().split()))

if S==0 and M==1:
  print('0 0')
  return
elif S==0 or M*9 < S:
  print('-1 -1')
  return

m,s=M,S
l=[]
if s<=(m-1)*9+1:
  l.append(1)
  s-=1
while len(l)<m:
  r = (m-len(l)-1)*9
  if s<=r:
    l.append(0)
  else:
    l.append(s-r)
    s-=s-r

m,s=M,S
h=[]
while s>=9:
  h.append(9)
  s-=9
while len(h)<m:
  h.append(s)
  s=0

print(''.join(repr(x) for x in l), ''.join(repr(x) for x in h))