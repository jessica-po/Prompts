#ABC147　C　やってる途中
n=int(input())
l=[]
for i in range(n):
  a=int(input())
  l_=[]
  for j in range(a):
    xy=list(map(int,input().split()))
    l_.append(xy)
  l.append(l_)
ans=0
for i in range(2**n):
  table=[0]*n
  flag=False
  for j in range(n):
    if (i>>j)&1:
      table[j]=1
  for j in range(n):
    for k in l[j]:
   
      if k[1]!=table[k[0]-1] and table[j]==1:
        flag=True
        break

        if flag:
          break

  if flag==True:
    continue


  ans = max(ans, table.count(1))


print(ans)