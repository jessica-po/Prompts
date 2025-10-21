import sys
n,m=list(map(int,sys.stdin.readline().split()))

A=list(map(int,sys.stdin.readline().split()))

Ans=[1]

E={}
E[A[-1]]=1
for i in range(n-2,-1,-1):
    if(A[i] in E):
        Ans.append(Ans[-1])
    else:
        E[A[i]]=1
        Ans.append(Ans[-1]+1)

Answer=""
for i in range(m):
    x=int(sys.stdin.readline())
    x-=1
    x=n-1-x
    Answer+=str(Ans[x])+"\n"
sys.stdout.write(Answer)