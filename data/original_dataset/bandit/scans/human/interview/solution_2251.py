n, m = list(map(int, input().split()))
mx = [[0x00] * n for i in range(n)]
used = None

def dfs(cur, trg, color):
    if cur == trg:
        return True
    if not used[cur]:
        used[cur] = True
        for i in range(n):
            if mx[cur][i] & color:
                if dfs(i, trg, color):
                    return True
    return False

for i in range(m):
    a, b, c = [int(s) - 1 for s in input().split()]
    mx[a][b] |= 1 << c
    mx[b][a] |= 1 << c

q = int(input())
for i in range(q):
    u, v = [int(s) - 1 for s in input().split()]
    result = 0
    for j in range(m):
        used = [False] * n
        if dfs(u, v, 1 << j):
            result += 1
    print(result)