n,k=list(map(int,input().split()))
a=list(map(int,input().split()))
from collections import Counter
dic=Counter(a)
dic=sorted(list(dic.items()),key=lambda x:x[1])

ans=0
cnt=0
l=max(len(dic)-k,0)
for i in dic:
  if cnt==l:
    break
  ans=ans+i[1]
  cnt=cnt+1
print(ans)