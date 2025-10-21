import sys
input = sys.stdin.readline

n,m=list(map(int,input().split()))
mod=998244353

FACT=[1]
for i in range(1,2*10**5+1):
    FACT.append(FACT[-1]*i%mod)

FACT_INV=[pow(FACT[-1],mod-2,mod)]
for i in range(2*10**5,0,-1):
    FACT_INV.append(FACT_INV[-1]*i%mod)

FACT_INV.reverse()

def Combi(a,b):
    if 0<=b<=a:
        return FACT[a]*FACT_INV[b]*FACT_INV[a-b]%mod
    else:
        return 0

if n==2:
    print(0)
else:
    print(Combi(m,n-1)*(n-2)*pow(2,n-3,mod)%mod)