t=1
for _ in range(t):
    n,m,k=(list(map(int,input().split())))
    a=list(map(int,input().split()))
    for i in range(n):
        a[i]=a[i]%k
    
    s=1
    for j in range(k):
        ss=0
        v=0
        for i in range(n):
            v+=min(abs(a[i]-j),k-abs(a[i]-j))
            while ss<i and v>m:
                v-=min(abs(a[ss]-j),k-abs(a[ss]-j))
                ss+=1
            s=max(s,i-ss+1)
        
    print(s)