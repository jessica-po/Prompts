N=int(input())
mod=998244353
inv4=249561088
A=[inv4,0,3]
for i in range(N):
    A.append(9*A[-1]-24*A[-2]+16*A[-3])
    A[-1]%=mod
A[0]-=inv4
B=[0 for i in range(N)]
for i in range(N):
    x=i
    y=N-i-1
    if x<=y:
        B[x]=A[i]
        B[y]=A[i]

P=N*pow(2,N-2+mod-1,mod)
for i in range(N):
    B[i]+=P
    B[i]%=mod
Q=pow(2,N-1,mod)
Qinv=pow(Q,mod-2,mod)
for i in range(N):
    B[i]*=Qinv
    B[i]%=mod
for i in range(N):
    print((B[i]))