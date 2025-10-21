n, m = [int(i) for i in input().split()]
A = []
C = []
for i in range(n):
    B = [int(j) for j in input().split()]
    A.append(B)
    C.append(sorted(list(set(B))))

xor = 0
ans = []

for i in range(n):
    xor ^= A[i][0]
    ans.append(1)

if xor==0:
    found = 0
    for trial in range(n-1, -1, -1):
        newxor = xor^A[trial][0]
        if found==1:
            break
        for j in range(m):
            if A[trial][j]^newxor!=0:
                ans[trial] = j+1
                found = 1
                break
        if found==1:
            break
    if found:
        print('TAK')
        print(*ans)
    else:
        print('NIE')
else:
    print('TAK')
    print(*ans)