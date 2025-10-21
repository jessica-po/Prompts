a,b,x,y = map(int, input().split())
y=min(y,2*x)

if a==b or a==b+1:
    print(x)
    return

ans=x+abs(a-b)*y
if a>b:
    ans-=y
print(ans)