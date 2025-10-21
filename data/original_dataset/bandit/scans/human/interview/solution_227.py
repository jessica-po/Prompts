def Solve(x,B):
    if((X,x,B) in Mem):
        return Mem[(X,x,B)]
    if(len(B)>X):
        return False
    if(x==len(L)):
        return True
    if(Form(L[x],B)):
        A=list(B)
        for e in range(len(B)):
            r=A[e]
            A[e]=L[x]
            if(Solve(x+1,tuple(sorted(A)))):
                Mem[(X,x,B)]=True
                return True
            A[e]=r
        A+=[L[x]]
        if(Solve(x+1,tuple(sorted(A)))):
            Mem[(X,x,B)]=True
            return True
    Mem[(X,x,B)]=False
    return False

def Form(x,B):
    for i in range(len(B)):
        for j in range(i,len(B)):
            if(B[i]+B[j]==x):
                return True
    return False
        
n=int(input())
L=list(map(int,input().split()))
done=False
Mem={}
for X in range(1,n+1):
    if(Solve(1,(L[0],))):
        print(X)
        done=True
        break
if(not done):
    print(-1)