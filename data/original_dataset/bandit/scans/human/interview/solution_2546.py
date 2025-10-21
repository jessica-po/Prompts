import sys
input = sys.stdin.readline

t=int(input())

for test in range(t):

    n,s=list(map(int,input().split()))
    LR=[tuple(map(int,input().split())) for i in range(n)]
    LR.sort(reverse=True)

    R=[r for l,r in LR]
    R.sort()

    #print(LR,R)

    MIN=LR[n//2][0]
    MAX=R[n//2]
    
    OK=(n+1)//2

    while MIN!=MAX:
        mid=(MIN+MAX+1)//2
        #print(MIN,MAX,mid)
        count=0
        money=0

        for l,r in LR:

            if count<OK:
                if r>=mid:
                    money+=max(l,mid)
                    count+=1
                else:
                    money+=l

            else:
                money+=l

        if count>=OK and money<=s:
            MIN=mid
        else:
            MAX=mid-1

    print(MIN)