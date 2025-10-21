n=int(input())

L=[]
for i in range(n):
    L.append(input())
valid=True
x=0
y=0
E=[]
p=L[0][0]
while(x<n and y<n):
    if(L[x][y]!=p):
        valid=False
    x+=1
    y+=1
    
x=0
y=n-1

while(x<n and y>=0):
    if(L[x][y]!=p):
        valid=False
    x+=1
    y-=1
K={}
for i in range(n):
    for j in range(n):
        if(L[i][j] in K):
            K[L[i][j]]+=1
        else:
            K[L[i][j]]=1


if(not valid or K[p]!=2*n-1 or len(K)!=2):
    print("NO")

else:
    print("YES")