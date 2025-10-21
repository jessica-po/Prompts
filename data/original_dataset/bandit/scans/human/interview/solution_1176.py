n=int(input())
a=list(map(int,input().split()))
count=0
ans=[]
for i in range(n):
  ans.append(abs(a[i]))
  if a[i]<0:
    count+=1

if count%2==0:
  print((sum(ans)))
else:
  print((sum(ans)-2*min(ans)))