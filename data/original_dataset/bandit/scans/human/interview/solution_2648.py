n=int(input())
a=list(map(int,input().split()))
num=[0]*100001
for i in a:
  num[i]+=1
x=0
for i in num:
  if i<=0:
    continue
  elif i%2==0:
    n-=i
    x+=1
  else:
    n-=i-1
    
if x%2:
  x-=1
  
print(n+x)