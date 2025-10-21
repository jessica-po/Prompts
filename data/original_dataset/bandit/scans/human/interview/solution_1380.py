n,k=map(int,input().split())
a=list(map(int,input().split()))
p=1000
first=1
for i in range(n):
    if a[i]>k*i:
        now=0
        f=a[i]-k*i
        for j in range(i):
            if a[j]!=f+k*j:
                now+=1
        for j in range(i+1,n):
            if a[j]!=f+j*k:
                now+=1
        if now<p:
            p=now
            first=f
print(p)
for i in range(n):
    if a[i]!=first+k*i:
        print('+' if a[i]<first+k*i else '-',i+1,abs(a[i]-first-k*i))