from math import *

c=int(input())
x=[0]*c
y=[0]*c
vu=[False]*c
for i in range(c):
    x[i],y[i]=[int(s) for s in input().split()]
prix=[int(s) for s in input().split()]
fil=[int(s) for s in input().split()]
anc=[-1]*c
pmin=prix.copy()
v=0
pl=[]
e=0
ppl=[]
tot=0
for i in range(c):
    pmina=100000000000000000000000
    for j in range(c):
        if (not vu[j]) and pmin[j]<pmina:
            pmini=j
            pmina=pmin[j]
    vu[pmini]=True
    tot+=pmina
    if anc[pmini]==-1:
        v+=1
        pl.append(str(pmini+1))
    else:
        e+=1
        ppl.append([str(pmini+1),str(anc[pmini]+1)])
    for j in range(c):
        if (abs(x[pmini]-x[j])+abs(y[pmini]-y[j]))*(fil[pmini]+fil[j])<pmin[j]:
            pmin[j]=(abs(x[pmini]-x[j])+abs(y[pmini]-y[j]))*(fil[pmini]+fil[j])
            anc[j]=pmini
print(tot)
print(v)
print(" ".join(pl))
print(e)
for i in ppl:
    print(" ".join(i))