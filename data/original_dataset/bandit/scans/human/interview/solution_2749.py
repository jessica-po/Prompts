h, w = map(int, input().split())
n = int(input())
A = tuple(map(int, input().split()))

M = [[0] * w for _ in range(h)]
ii = 0
ij = 0
for i, a in enumerate(A):
    i += 1
    for _ in range(a):
        M[ij][ii] = i

        if ij%2 == 0:
            ii += 1
            if ii == w:
                ij += 1
                ii = w-1
        else:
            ii -= 1
            if ii == -1:
                ij += 1
                ii = 0
for l in M:
    print(*l)