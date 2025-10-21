n=int(input())
a=(list(map(int,input().split())))
a.sort(reverse=True)
x,f=list(map(int,input().split()))
ans=0
for i in range(n):
    if a[i]>x:
        r=(a[i]-x)//(x+f)
        if (a[i]-x)%(x+f):
            r+=1
        ans+=(f*r)
    else:
        break
print(ans)