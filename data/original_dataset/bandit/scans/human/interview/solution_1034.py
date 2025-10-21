X,Y,Z,K = list(map(int, input().split()))

A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))

A.sort(reverse=True)
B.sort(reverse=True)
C.sort(reverse=True)


ans = []
for i in range(X):
    if (i+1) > K: break
    for j in range(Y):
        if (i+1)*(j+1) > K: break
        for k in range(Z):
            if (i+1)*(j+1)*(k+1) > K: break
            ans.append(A[i]+B[j]+C[k])

ans.sort(reverse=True)

for i in range(K):
    print((ans[i]))