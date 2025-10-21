from math import inf
n=int(input())

a = input()
a= [int(i) for i in a.split()]
s  =input()
s  = [int(i) for i in s.split()]
ans  =  inf
for j in range(1 , n-1):
    ll , lr = inf , inf
    for q in range(j+1,n):
        if a[j]<a[q]:
            lr = min(lr , s[q])
    for q in range(j):
        if a[j]>a[q]:
            ll = min(ll , s[q]) 
    ans= min(ans , ll+lr+s[j])
if ans==inf:
    print(-1)
else:
    print(ans)