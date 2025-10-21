import sys
input = sys.stdin.readline

t=int(input())
for testcases in range(t):
    n=int(input())

    LIST=[input().strip() for i in range(n)]
    SET=set()

    ANS=0
    CHANGE=set()
    for i in range(n):
        if LIST[i] in SET:
            ANS+=1
            CHANGE.add(i)
        else:
            SET.add(LIST[i])

    ALIST=[]

    for i in range(n):
        if i in CHANGE:
            flag=0
            now=LIST[i]
            
            for j in range(4):
                for k in range(10):
                    x=now[:j]+str(k)+now[j+1:]

                    if x in SET:
                        continue
                    else:
                        ALIST.append(x)
                        SET.add(x)
                        flag=1
                        break
                if flag:
                    break

        else:
            ALIST.append(LIST[i])
    print(ANS)
    print("\n".join(ALIST))