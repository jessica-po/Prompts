n,m=list(map(int,input().split()))
if(m!=0):
    L=list(map(int,input().split()))
else:
    L=[]

L.sort()
valid=True
for i in range(2,m):
    if(L[i]-L[i-2]==2):
        valid=False
if(m==0 or(valid and L[0]!=1 and L[-1]!=n)):
    print("YES")
else:
    print("NO")