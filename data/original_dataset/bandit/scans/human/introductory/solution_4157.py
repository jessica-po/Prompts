def powof3(x):
    ans=0
    while(x%3==0):
        x=x//3
        ans+=1
    return ans


n=int(input())
a=list(map(int,input().split()))
for i in range(n):
    a[i]=[-1*powof3(a[i]),a[i]]
a.sort()
for i in range(n):
    a[i]=a[i][1]
print(*a)