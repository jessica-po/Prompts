import math as mt 
import sys,string
input=sys.stdin.readline
print=sys.stdout.write
import random
from collections import deque,defaultdict
L=lambda : list(map(int,input().split()))
Ls=lambda : list(input().split())
M=lambda : map(int,input().split())
I=lambda :int(input())
t=I()
d=defaultdict(str)
ml=0
p=0
for _ in range(t):
    s=input().split()
    w=s[0]
    x=list(map(int,s[1::]))
    for i in range(1,len(x)):
        r=d[x[i]-1]
        if(len(r)<len(w)):
            d[x[i]-1]=w
    ml=max(ml,len(w)+x[-1]-1)
ans="a"*ml
ans=list(ans)
#print(d)
p=-1
z=sorted(list(d.keys()))
for i in z:
    if(i+len(d[i])>p):
        if(i>=p):
            for j in range(i,i+len(d[i])):
                ans[j]=d[i][j-i]
        else:
            leave=p-i
            f=max(i,p)
            #print(ans,"@",d[i],p,d[i][leave::])
            for j in range(leave,len(d[i])):
                ans[f]=d[i][j]
                f+=1
            #print(ans,"*")
        p=i+len(d[i])
    
for i in ans:
    print(i)