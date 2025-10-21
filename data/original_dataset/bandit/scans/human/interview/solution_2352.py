import sys
input = sys.stdin.readline

testcases=int(input())

for testcase in range(testcases):
    n,m=list(map(int,input().split()))
    MAP=[input().strip() for i in range(n)]
    #print(MAP)

    STR=[[] for i in range(26)]

    for i in range(n):
        for j in range(m):
            if MAP[i][j]!=".":
                STR[ord(MAP[i][j])-97].append([i,j])

    #print(STR)

    for s in range(25,-1,-1):
        if STR[s]==[]:
            continue
        
        x,y=STR[s][0]
        z,w=STR[s][-1]
        flag=1
        
        if x==z:
            for k in range(y,w+1):
                if MAP[x][k]>=chr(s+97):
                    continue
                else:
                    flag=0
                    break
                
            for u,v in STR[s]:
                if u==x:
                    continue
                else:
                    flag=0
                    break

        elif y==w:
            for k in range(x,z+1):
                if MAP[k][y]>=chr(s+97):
                    continue
                else:
                    flag=0
                    break
                
            for u,v in STR[s]:
                if v==y:
                    continue
                else:
                    flag=0
                    break

        else:
            flag=0

        if flag==0:
            print("NO")
            break
    else:
        print("YES")

        for s in range(25,-1,-1):
            if STR[s]!=[]:
                ANS=s+1
                ANONE=STR[s][0]
                print(ANS)
                break
        else:
            print(0)
            continue

        for ans in range(ANS):
            if STR[ans]!=[]:
                print(STR[ans][0][0]+1,STR[ans][0][1]+1,STR[ans][-1][0]+1,STR[ans][-1][1]+1)
            else:
                print(ANONE[0]+1,ANONE[1]+1,ANONE[0]+1,ANONE[1]+1)