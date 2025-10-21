import sys
readline = sys.stdin.readline

H, W = map(int, readline().split())
G = [[1 if s == '#' else 0 for s in readline().strip()] for _ in range(H)]

DIREC = [(0, 1), (1, 0), (-1, 0), (0, -1)]
def calc():
    zh = 0      
    for i in range(H):
        cnt = 0
        for j in range(W):
            if G[i][j]:
                if cnt == 0:
                    cnt = 1
                    continue
                if cnt == 1:
                    continue
                if cnt == 2:
                    return -1
            else:
                if cnt == 0:
                    continue
                cnt = 2
        if cnt == 0:
            zh = 1
    zw = 0
    for j in range(W):
        cnt = 0
        for i in range(H):
            if G[i][j]:
                if cnt == 0:
                    cnt = 1
                    continue
                if cnt == 1:
                    continue
                if cnt == 2:
                    return -1
            else:
                if cnt == 0:
                    continue
                cnt = 2
        if cnt == 0:
            zw = 1
    if zw^zh:
        return -1
    ans = 0
    used = set()
    geta = W
    for i in range(H):
        for j in range(W):
            if G[i][j] == 0:
                continue
            if (i*geta + j) in used:
                continue
            ans += 1
            stack = [i*geta + j]
            while stack:
                nh, nw = divmod(stack.pop(), geta)
                for dh, dw in DIREC:
                    fh, fw = nh+dh, nw+dw
                    if not 0 <= fh < H or not 0 <= fw < W:
                        continue
                    if not G[fh][fw]:
                        continue
                    vf = fh*geta + fw
                    if vf in used:
                        continue
                    stack.append(vf)
                    used.add(vf)
    return ans
print(calc())