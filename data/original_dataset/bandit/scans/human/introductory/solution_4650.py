for i in range(int(input())):
    n=int(input())
    l1=list(map(int,input().split()))
    type1=0
    type2=0
    ans=0
    for item in l1:
        if item%3==0:
            ans+=1
        elif item%3==1:
            type1+=1
        else :
            type2+=1
    x=min(type1,type2)
    ans+=x
    type1-=x
    type2-=x
    ans+=(type1//3+type2//3)
    print(ans)