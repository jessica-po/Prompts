n,m,k = map(int, input().split())
mCnt = 0
ans = [0]*m
start = 0
end = 0
Q = [[] for i in range(m)]

for i in range(n):
    A = list(map(int, input().split()))
    z = 0
    for j in range(m) :
        while Q[j] and Q[j][-1][0] < A[j] :
            Q[j].pop()
        Q[j].append([A[j],i])
        z += Q[j][0][0]
    if z <= k :
        end = i+1
        if mCnt < end - start :
            mCnt = end - start
            for j in range(m) :
                ans[j] = Q[j][0][0]
    else :
        while True :
            z = 0
            for j in range(m) :
                if Q[j] and Q[j][0][1] == start :
                    Q[j].pop(0)
                if Q[j] : z += Q[j][0][0]
            start += 1
            if z<= k : break
        end += 1
            
for i in ans :
    print(i, end = " ")