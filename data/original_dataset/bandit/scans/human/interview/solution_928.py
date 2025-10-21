N,K=map(int,input().split())
A=list(map(int,input().split()))

l=0
r=0
s=A[0]
ans=0
while True:

    if s>=K:
        ans+=N-r
        s-=A[l]
        l+=1

    else:
        if r<N-1:
            r+=1
            s+=A[r]
        else:
            break
    
print(ans)