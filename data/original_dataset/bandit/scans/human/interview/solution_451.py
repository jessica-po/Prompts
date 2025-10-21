n,k = list(map(int, input().split()))
b = list(map(int,input().split()))

SSSSSSSSSS = input()

INF = 1000*1000*1000+123
RRRR = [];
WWWWWWW = [];
OOOOOOOOO = [];

for i in range(n):
    if SSSSSSSSSS[i] == 'R':
        RRRR.append(b[i])
    elif SSSSSSSSSS[i] == 'W':
        WWWWWWW.append(b[i])
    else:
        OOOOOOOOO.append(b[i])



WWWWWWW.sort()

RRRR.sort()
WWWWWWW.reverse()
RRRR.reverse()
OOOOOOOOO.sort()
OOOOOOOOO.reverse()

if k == 1:
    print(-1)
    return


def cccmcmc(A, B):
    qanakA = len(A);
    qanakB = len(B);

    pA = [0 for i in range(qanakA)]
    pB = [0 for i in range(qanakB)]
    pB[0] = B[0]
    pA[0] = A[0]

    for i in range(1,qanakA):
        pA[i] = pA[i-1] + A[i];
    for i in range(1,qanakB):
        pB[i] = pB[i-1] + B[i];

    res = -1

    for i in range(1,min(qanakA+1,k)):
        aic = pA[i-1]
        bepetk = k-i
        if bepetk <= 0 or bepetk > qanakB: continue
        bic = pB[bepetk-1]
        res = max(res,aic+bic)
    return res


res = -1

if len(WWWWWWW) > 0 and len(OOOOOOOOO)> 0:
    res = max(res, cccmcmc(WWWWWWW, OOOOOOOOO))
if len(RRRR) > 0 and len(OOOOOOOOO)> 0:
    res = max(res, cccmcmc(RRRR, OOOOOOOOO))

print(res)