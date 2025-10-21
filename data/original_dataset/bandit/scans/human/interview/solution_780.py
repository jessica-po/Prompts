S = input()

T = [[0]*10 for i in range(10)]

for i in range(1,len(S)):
    T[int(S[i-1])][int(S[i])]+=1

C = [[[[0 for i in range(10)] for j in range(10)] for k in range(10)] for l in range(10)]

for i in range(10):
    for j in range(10):
        for k in range(10):
            for l in range(10):
                min_val = 1000
                for a1 in range(11):
                    for a2 in range(11):
                        if a1!=0 or a2!=0:
                            if j==(a1*k+a2*l + i)%10:
                                min_val=min(min_val,a1+a2)
                if min_val==1000:
                    min_val = -10**10
                C[i][j][k][l] = min_val-1

ans = [[0]*10 for i in range(10)]

for k in range(10):
    for l in range(10):
        a = 0
        for i in range(10):
            for j in range(10):
                a+=C[i][j][k][l]*T[i][j]
        if a<0:
            a=-1
        ans[k][l] = a

for a in ans:
    print(*a)