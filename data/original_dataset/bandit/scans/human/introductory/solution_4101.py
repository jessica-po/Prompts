import sys
input = sys.stdin.readline

n,m=list(map(int,input().split()))
A=[list(map(int,input().split())) for i in range(n)]

for i in range(m):
    #一行目をi-1まで0にする

    ANSR=[0]*n
    ANSC=[0]*m

    for j in range(i):
        if A[0][j]==1:
            ANSC[j]=1

    for j in range(i,m):
        if A[0][j]==0:
            ANSC[j]=1

    for r in range(1,n):
        B=set()
        for c in range(m):
            if ANSC[c]==0:
                B.add(A[r][c])
            else:
                B.add(1-A[r][c])

        if len(B)>=2:
            break
        if max(B)==0:
            ANSR[r]=1

    else:
        print("YES")
        print("".join(map(str,ANSR)))
        print("".join(map(str,ANSC)))
        return

ANSR=[0]*n
ANSC=[0]*m

for j in range(m):
    if A[0][j]==1:
        ANSC[j]=1

flag=0
for r in range(1,n):
    if flag==0:
        B=[]
        for c in range(m):
            if ANSC[c]==0:
                B.append(A[r][c])
            else:
                B.append(1-A[r][c])

        if max(B)==0:
            continue
        elif min(B)==1:
            ANSR[r]=1
            continue
        else:
            OI=B.index(1)
            if min(B[OI:])==1:
                flag=1
                continue

            OO=B.index(0)
            if max(B[OO:])==0:
                flag=1
                ANSR[r]=1
                continue

            else:
                print("NO")
                return

    else:

        B=set()
        for c in range(m):
            if ANSC[c]==0:
                B.add(A[r][c])
            else:
                B.add(1-A[r][c])

        if len(B)>=2:
            break
        if max(B)==0:
            ANSR[r]=1

else:
    print("YES")
    print("".join(map(str,ANSR)))
    print("".join(map(str,ANSC)))
    return

print("NO")