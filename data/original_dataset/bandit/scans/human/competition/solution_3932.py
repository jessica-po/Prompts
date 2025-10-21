def DFS(x):
    for i in range(x):
        if(Seen[i][x]):
            continue
        if(Rem[i]>=C[x]):
            if(Rem[i]==C[x] and len(Children[i])==0):
                continue
            Rem[i]-=C[x]
            Parent[x]=i
            Children[i].append(x)
            return True
    for i in range(x):
        if(Seen[i][x]):
            continue
        Y=[]
        for j in range(len(Children[i])):
            child=Children[i][j]
            Parent[child]=-1
            Rem[i]+=C[child]
            Seen[i][child]=True
            Seen[child][i]=True
            if(DFS(child)):
                Seen[i][child]=False
                Seen[child][i]=False
                continue
            Seen[i][child]=False
            Seen[child][i]=False
            Parent[child]=i
            Rem[i]-=C[child]
            Y.append(child)
        Children[i]=list(Y)
        if(Rem[i]>=C[x]):
            if(Rem[i]==C[x] and len(Children[i])==0):
                continue
            Rem[i]-=C[x]
            Children[i].append(x)
            Parent[x]=i
            return True
    return False
                
        




n=int(input())

C=list(map(int,input().split()))
Rem=[-1]*n
Parent=[-1]*n
Children=[]
Seen=[]
for i in range(n):
    Seen.append([False]*n)
C.sort(reverse=True)

if(C[0]!=n or C.count(2)>0):
    print("NO")

else:
    for i in range(n):
        Rem[i]=C[i]-1
        Children.append([])
    Parent[0]=0
    Ans="YES"
    for i in range(1,n):
        if(DFS(i)==False):
            Ans="NO"
            break
    for i in range(n):
        if(Rem[i]!=0 and C[i]!=1):
            Ans="NO"
            break
    print(Ans)