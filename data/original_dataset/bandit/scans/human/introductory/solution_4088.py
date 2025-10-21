import sys
input = sys.stdin.readline

t=int(input())
for tests in range(t):
    S=input().strip()
    m=int(input())
    B=list(map(int,input().split()))

    LIST=[0]*26

    for s in S:
        LIST[ord(s)-97]+=1

    ANS=[0]*m
    ind=25

    while max(B)>=0:
        L=[]
        for i in range(m):
            if B[i]==0:
                L.append(i)
                B[i]=-1

        LEN=len(L)

        while LIST[ind]<LEN:
            ind-=1

        for l in L:
            ANS[l]=ind

        ind-=1

        for l in L:
            for i in range(m):
                B[i]-=abs(i-l)

    #print(ANS)
    print("".join([chr(a+97) for a in ANS]))