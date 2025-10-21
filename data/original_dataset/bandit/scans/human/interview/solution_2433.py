for i in range(int(input())):
    a,b,c=map(int,input().split())
    x,y=map(int,input().split())
    ans=0
    if x>y:
        ans=ans+x*min(a//2,b)
        a=(a-2*min(a//2,b))
        ans=ans+y*min(a//2,c)
    else :
        ans=ans+y*min(a//2,c)
        a=(a-2*min(a//2,c))
        ans=ans+x*min(a//2,b)
    print(ans)