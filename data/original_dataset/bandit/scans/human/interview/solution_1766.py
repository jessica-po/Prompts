n=int(input())
a=list(map(int,input().split()))
b=True
l=0
r=n-1
ans1=0
ans2=0
while l<=r:
    if a[l]>a[r]:
        if b:
            ans1+=a[l]
            b=False
        else:
            ans2+=a[l]
            b=True
        l+=1
    else:
        if b:
            ans1+=a[r]
            b=False
        else:
            ans2+=a[r]
            b=True   
        r-=1
print(ans1,ans2)