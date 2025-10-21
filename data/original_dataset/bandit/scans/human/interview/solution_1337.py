n = int(input())
L = list(map(int, input().split()))
m = int(input())
A = list(map(int, input().split()))
S = list(map(int, input().split()))

D = {}
for i in range(n):
    if L[i] in list(D.keys()):
        D[L[i]] += 1
    else:
        D[L[i]] = 1
M = [[0,0,i+1] for i in range(m)]
for i in range(m):
    if A[i] in list(D.keys()):
        M[i][0] += D[A[i]]
    if S[i] in list(D.keys()):
        M[i][1] += D[S[i]]

def ct(a):
    return a[0],a[1]

M.sort(key=ct,reverse=True)
print(M[0][2])