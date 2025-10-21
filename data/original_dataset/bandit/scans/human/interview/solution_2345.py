import sys
input = sys.stdin.readline

t=int(input())
for test in range(t):
    n=int(input())
    A=list(map(int,input().split()))

    ANS=[]
    SET=set()

    NOW=1
    while not (NOW in SET):
        ANS.append(NOW)
        SET.add(NOW)
        NOW=NOW-A[NOW-1]

    x=ANS.index(NOW)

    print(len(ANS[x:]))
    print(*ANS[x:])