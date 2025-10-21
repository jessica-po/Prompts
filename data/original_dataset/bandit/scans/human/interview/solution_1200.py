def gcd(a, b):
    if(a==0):
        return b
    return gcd(b%a, a)    

n=int(input())
v=list(map(int,input().split()))
v.sort()
ans=v[1]-v[0]
for i in range(2, n):
    ans=gcd(ans, v[i]-v[i-1])
print((v[len(v)-1]-v[0])//ans+1-n)