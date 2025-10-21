n,k=list(map(int,input().split()))
a=list(map(int,input().split()))
prefix=[a[0]]
for i in range(1,n):
    prefix.append(prefix[-1]+a[i])
ans=[]
for i in range(n):
    for j in range(i+k-1,n):
        if(i==0):
            ans.append(prefix[j]/(j-i+1))
        else:
            ans.append((prefix[j]-prefix[i-1])/(j-i+1))
print(max(ans))