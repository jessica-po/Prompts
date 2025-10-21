import sys
n,m=map(int,input().split())
red=[]

for i in range(n):
    a,b=map(int,input().split())
    red.append(a*b)

d={}
for i in range(m):
    a,b=map(int,input().split())
    p=a*b
    if p in d:
        d[p]+=1
    else:
        d[p]=1

an=0
for i in range(n):
    if red[i] in d and d[red[i]]>0:
        an+=1
        d[red[i]]-=1
    
print(an)