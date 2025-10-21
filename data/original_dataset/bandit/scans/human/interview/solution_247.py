n = int(input())
L = [(0, 0)] * n
for i in range(n):
    t = input().split(' ')
    a = int(t[0])
    b = int(t[1])
    L[i] = (a, b)
if n <= 4:
    print("YES")
else:
    b0 = True
    b1 = True
    b2 = True
    L0 = []
    L1 = []
    L2 = []
    for j in range(n):
        if (L[0][0]-L[1][0])*(L[0][1]-L[j][1])!=(L[0][1]-L[1][1])*(L[0][0]-L[j][0]):
            L2.append(L[j])
        if (L[2][0]-L[0][0])*(L[2][1]-L[j][1])!=(L[2][1]-L[0][1])*(L[2][0]-L[j][0]):
            L1.append(L[j])
        if (L[2][0]-L[1][0])*(L[2][1]-L[j][1])!=(L[2][1]-L[1][1])*(L[2][0]-L[j][0]):
            L0.append(L[j])
    if len(L0) >= 3:
        for j in range(2, len(L0)):
            if (L0[0][0]-L0[1][0])*(L0[0][1]-L0[j][1])!=(L0[0][1]-L0[1][1])*(L0[0][0]-L0[j][0]):
                b0 = False
    if len(L1) >= 3:
        for j in range(2, len(L1)):
            if (L1[0][0]-L1[1][0])*(L1[0][1]-L1[j][1])!=(L1[0][1]-L1[1][1])*(L1[0][0]-L1[j][0]):
                b1 = False
    if len(L2) >= 3:
        for j in range(2, len(L2)):
            if (L2[0][0]-L2[1][0])*(L2[0][1]-L2[j][1])!=(L2[0][1]-L2[1][1])*(L2[0][0]-L2[j][0]):
                b2 = False
    if b0 or b1 or b2:
        print("YES")
    else:
        print("NO")