import sys
input = sys.stdin.readline

q=int(input())
for testcase in range(q):
    n=int(input())
    A=sorted(set(map(int,input().split())),reverse=True)
    L=len(A)

    #print(A)
    ANS=A[0]
    for i in range(L):
        NOW0=A[i]
        NOW1=0

        flag=0
        for j in range(i+1,L):
            if NOW0%A[j]!=0:
                NOW1=A[j]
                ANS=max(ANS,NOW0+NOW1)

                for k in range(j+1,L):
                    if NOW0%A[k]!=0 and NOW1%A[k]!=0:
                        ANS=max(ANS,NOW0+NOW1+A[k])
                        #print("!",ANS)
                        break

                break

    print(ANS)