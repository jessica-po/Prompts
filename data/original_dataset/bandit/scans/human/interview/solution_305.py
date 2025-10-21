a=int(input())
b=int(input())
c=int(input())
d=int(input())
e=int(input())
f=int(input())
if e>=f:
    ans=min(a,d)
    d-=ans
    a-=ans
    ans*=e
    ans+=min(d,b,c)*f
else:
    ans=min(d,b,c)
    d-=ans
    ans*=f
    ans+=min(a,d)*e
print(ans)