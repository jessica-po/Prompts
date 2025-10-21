s=input()

if(len(s)<=3):
    print(0)

else:
    n=len(s)
    ans=0
    A=0
    for i in range(3,n):
        if(s[i-3]+s[i-2]+s[i-1]+s[i]=='bear'):
            ans+=((i-3)-A+1)*(n-i)
            A=i-2
    print(ans)