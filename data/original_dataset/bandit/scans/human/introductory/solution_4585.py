x=int(input())
ans=0
a=0
for i in range(1,x+1):
  a+=i
  ans+=1
  if a>=x:
    print(ans)
    break