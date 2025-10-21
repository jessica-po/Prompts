n=int(input())
val=list(map(int,input().split()))
b=list(map(int,input().split()))
neig=[0]*n
for i in range(n):
    neig[i]=[0]
inedges=[0]*n
for i in range(n):
    if b[i]!=-1:
        neig[i][0]+=1
        neig[i].append(b[i]-1)
        inedges[b[i]-1]+=1
ans=0
beg=[]
en=[]
tod=[]
for i in range(n):
    if inedges[i]==0:
        tod.append(i)
while len(tod)>0:
    x=tod.pop()
    ans+=val[x]
    if val[x]>0:
        beg.append(x+1)
    else:
        en.append(x+1)
    if neig[x][0]==1:
        inedges[neig[x][1]]-=1
        if inedges[neig[x][1]]==0:
            tod.append(neig[x][1])
        if val[x]>0:
            val[neig[x][1]]+=val[x]
print(ans)
print(*beg,end=" ")
en.reverse()
print(*en)