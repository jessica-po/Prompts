from itertools import permutations

n = int(input())

p1, _, p2, _, p3, _, p4 = [input() for _ in range(n)], input(), [input() for _ in range(n)], input(), [input() for _ in range(n)], input(), [input() for _ in range(n)]

def count(a,b,c,d):
    board = [a[i] + b[i] for i in range(n)] + [c[i] + d[i] for i in range(n)]

    res = 0
    for i in range(2*n):
        for j in range(2*n):
            clr = '1' if (i+j)%2 == 0 else '0'
            res += board[i][j] != clr
    return res

print(min(count(*p) for p in permutations([p1, p2, p3, p4])))