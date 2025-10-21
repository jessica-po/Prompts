n=int(input())

L=list(map(int,input().split()))

T=int(input())

X=[0]*1005

for i in range(len(L)):
    X[L[i]]+=1

for i in range(1,1005):
    X[i]+=X[i-1]
best=0
for i in range(1+T,1005):
    if(X[i]-X[i-T-1]>best):
        best=X[i]-X[i-T-1]
print(best)