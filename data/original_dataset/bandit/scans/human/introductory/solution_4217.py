from collections import Counter

n,m=map(int,input().split())

lis=[]
cnt=0
for i in range(n):
  l=list(map(int,input().split()))
  lis+=l[1:]
  
d=Counter(lis)
for i in d.values():
  if i==n:
    cnt+=1
    
print(cnt)