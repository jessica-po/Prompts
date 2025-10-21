a1=int(input())
a2=int(input())
k1=int(input())
k2=int(input())
n=int(input())
ans1=0
ans2=0

if k1<k2:
    ans1+=min(n//k1,a1)
    ans1+=(n-ans1*k1)//k2
else :
    ans1+=min(n//k2,a2)
    ans1+=(n-ans1*k2)//k1
ans2=max(0,n-(k1-1)*a1-(k2-1)*a2)
print(ans2,ans1)