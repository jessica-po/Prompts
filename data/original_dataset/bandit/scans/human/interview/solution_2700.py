T=eval(input())
for i in range(T):
 a,b,c,d=list(map(int,input().split()))
 x=c-a
 n1=b-a+1
 n2=d-c+1
 s=0
 if x<=0:
  t=n2-abs(x)-1
  for j in range(t,max(0,d-b-1),-1):
   s=s+j
 if x>0:
  t=n2
  for j in range(x,max(0,c-b-1),-1):
   s=s+t
  if (c-b)<=0:
   for j in range(t-1,max(0,d-b-1),-1):
    s=s+j
 print(s)