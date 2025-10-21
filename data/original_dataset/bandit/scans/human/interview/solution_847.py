n,x=list(map(int,input().split()))

L=list(map(int,input().split()))

s=sum(L)

s=abs(s)
ans=0
while(s>0):
    s-=x
    ans+=1
print(ans)