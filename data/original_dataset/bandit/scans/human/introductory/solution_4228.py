n,l=map(int,input().split())
c=0
m=100000
for i in range(1,n+1):
  c+=l+i-1
  m=min(m,abs(l+i-1))
if l<0 and l-n<=0:
  print(c+m)
else:
  print(c-m)