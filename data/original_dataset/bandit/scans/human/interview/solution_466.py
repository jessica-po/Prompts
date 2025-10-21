c,d=list(map(int,input().split()))

n,m=list(map(int,input().split()))

k=int(input())

z=0
best=10**10
while(1):
    x=n*m-k
    x-=z*n
    best=min(best,z*c+(max(x,0)*d))
    if(x<0):
        break
    z+=1
print(best)