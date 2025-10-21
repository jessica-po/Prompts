N=int(input())
A=list(map(int,input().split()))
B=list(map(int,input().split()))

A.append(A[0])
B.append(B[0])

AX=[]
BX=[]
for i in range(N):
    AX.append(A[i]^A[i+1])
    BX.append(B[i]^B[i+1])

AX+=AX+[AX[0]]

# Rolling Hashで。

p=1<<30
mod=(1<<62)+1 # Hashがぶつからない, pと互いに素な数を適当に指定

A_TABLE=[0] # Rolling Hashのテーブル. 最初は0
B_TABLE=[0] # Rolling Hashのテーブル. 最初は0

for i in range(len(AX)):
    A_TABLE.append((p*A_TABLE[-1]%mod+AX[i])%mod) # テーブルを埋める

for i in range(len(BX)):
    B_TABLE.append((p*B_TABLE[-1]%mod+BX[i])%mod) # テーブルを埋める

def hash(i,j): # [i,j)のハッシュ値を求める
    return (A_TABLE[j]-A_TABLE[i]*pow(p,j-i,mod))%mod

BH=B_TABLE[-1]
ANS=[]
for i in range(N):
    if hash(i,i+N)==BH:
        ANS.append((i,A[i]^B[0]))

for a in ANS:
    print(*a)