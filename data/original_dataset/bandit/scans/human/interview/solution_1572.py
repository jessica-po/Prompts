n=int(input())

L=list(map(int,input().split()))

if(n==1 or n==2):
    print(n)
else:
    length=2
    i=2
    maxx=2
    while(i<n):
        if(L[i]==L[i-1]+L[i-2]):
            length+=1
        else:
            if(length>maxx):
                maxx=length
            length=2
        i+=1
    if(length>maxx):
        maxx=length
    print(maxx)