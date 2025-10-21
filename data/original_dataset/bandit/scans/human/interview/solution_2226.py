import sys
input = sys.stdin.readline
#lev contains height from root,lower neighbour, higher neighbours
#lev[0] contains 0 (because it is the root), higher neighbours (=neighbours)
n,m,q=map(int,input().split())
mod=1000000007
mxw=0
wgts=[0]*n
neig=[0]*n
for i in range(n):
    neig[i]=[0]

for i in range(m):
    a,b,w=map(int,input().split())
    a-=1
    b-=1
    neig[a][0]+=1
    neig[b][0]+=1
    neig[a].append([b,w])
    neig[b].append([a,w])
    mxw=max(mxw,w)
    wgts[a]=max(wgts[a],w)
    wgts[b]=max(wgts[b],w)
poss=[-1]*n
poss[0]=0
sol=0
curw=0
hasmxw=[False]*n
for i in range(n):
    if wgts[i]==mxw:
        hasmxw[i]=True
ov=False
l=0
while l<q and not ov and l<3000:
    newposs=[-1]*n
    for i in range(n):
        if poss[i]>=0:
            for j in range(1,neig[i][0]+1):
                newposs[neig[i][j][0]]=max(newposs[neig[i][j][0]],poss[i]+neig[i][j][1])
    curmx=0
    for i in range(n):
        poss[i]=newposs[i]
        if poss[i]>curmx:
            curmx=poss[i]
            ov=hasmxw[i]
        else:
            if poss[i]==curmx and hasmxw[i]:
                ov=True
    curw=curmx
    sol+=curw
    sol%=mod
    l+=1
if l==q:
    print(sol)
else:
    if ov:
        rem=q-l
        sol+=rem*curw
        sol%=mod
        sol+=mxw*((rem*(rem+1))//2)
        sol%=mod
        print(sol)
    else:
        rem=q-l
        while not ov:
            mx=0
            for i in range(n):
                if poss[i]==curw:
                    mx=max(mx,wgts[i])
            gd=-1
            for i in range(n):
                if wgts[i]>mx and poss[i]>=0:
                    diff=wgts[i]-mx
                    loss=curw-poss[i]
                    loss+=diff-1
                    att=loss//diff
                    if gd==-1:
                        gd=att
                    gd=min(att,gd)
            if gd==-1 or gd>rem:
                sol+=rem*curw
                sol+=mx*((rem*(rem+1))//2)
                sol%=mod
                ov=True
            else:
                sol+=(gd-1)*curw
                sol+=mx*((gd*(gd-1))//2)
                sol%=mod
                for i in range(n):
                    poss[i]+=gd*wgts[i]
                    curw=max(curw,poss[i])
                sol+=curw
                rem-=gd
        print(sol)