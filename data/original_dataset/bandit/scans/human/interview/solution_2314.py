import sys
readline = sys.stdin.readline

def accumulate2d(X):
    N = len(X)
    M = len(X[0])
    
    for i in range(0, N):
        for j in range(1, M):
            X[i][j] += X[i][j-1]
    
    for j in range(0, M):
        for i in range(1, N):
            X[i][j] += X[i-1][j]
    
    return X

N, M, Q = map(int, readline().split())
table = [None]*100
table[ord('R')] = 0
table[ord('G')] = 1
table[ord('B')] = 2
table[ord('Y')] = 3

INF = 10**3
D = [[table[ord(s)] for s in readline().strip()] for _ in range(N)]
G = [[0]*M for _ in range(N)]

BS = 25
candi = []
geta = M
for i in range(N-1):
    for j in range(M-1):
        if D[i][j] == 0 and D[i][j+1] == 1 and D[i+1][j+1] == 2 and D[i+1][j] == 3:
            G[i][j] = 1
            nh, nw = i, j
            while True:
                k = G[nh][nw]
                fh, fw = nh-k, nw-k
                k2 = 2*(k+1)
                kh = k+1
                if fh < 0 or fw < 0 or N < fh+k2-1 or M < fw+k2-1:
                    break
                if any(D[fh][j] != 0 for j in range(fw, fw+kh)) or\
                any(D[j][fw] != 0 for j in range(fh, fh+kh)) or\
                any(D[fh][j] != 1 for j in range(fw+kh, fw+k2)) or\
                any(D[j][fw+k2-1] != 1 for j in range(fh, fh+kh)) or\
                any(D[j][fw+k2-1] != 2 for j in range(fh+kh, fh+k2)) or\
                any(D[fh+k2-1][j] != 2 for j in range(fw+kh, fw+k2)) or\
                any(D[fh+k2-1][j] != 3 for j in range(fw, fw+kh)) or\
                any(D[j][fw] != 3 for j in range(fh+kh, fh+k2)):
                    break
                G[nh][nw] += 1
            if G[nh][nw] > BS:
                candi.append((nh, nw))

 
Gnum = [None] + [[[0]*M for _ in range(N)] for _ in range(BS)]
for h in range(N):
    for w in range(M):
        if G[h][w] > 0:
            for k in range(1, min(BS, G[h][w])+1):
                Gnum[k][h][w] = 1

Gnum = [None] + [accumulate2d(g) for g in Gnum[1:]]


Ans = [None]*Q
for qu in range(Q):
    h1, w1, h2, w2 = map(lambda x: int(x)-1, readline().split())
    res = 0
    for k in range(min(BS, h2-h1+1, w2-w1+1), 0, -1):
        hs, ws = h1+k-1, w1+k-1
        he, we = h2-k, w2-k
        if hs <= he and ws <= we:
            cnt = Gnum[k][he][we]
            if hs:
                cnt -= Gnum[k][hs-1][we]
            if ws:
                cnt -= Gnum[k][he][ws-1]
            if hs and ws:
                cnt += Gnum[k][hs-1][ws-1]
            if cnt:
                res = k
                break
    
    for nh, nw in candi:
        if h1 <= nh <= h2 and w1 <= nw <= w2:
            res = max(res, min(nh-h1+1, h2-nh, nw-w1+1, w2-nw, G[nh][nw]))
    Ans[qu] = 4*res**2
print('\n'.join(map(str, Ans)))