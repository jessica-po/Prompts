from collections import defaultdict
import itertools
n, c = map(int, input().split())
D = [list(map(int, input().split()))for _ in range(c)]

# 集計
diago = [defaultdict(int)for _ in range(3)]
for i in range(n):
    for j, color in enumerate(map(int, input().split())):
        color -= 1
        if (i+j) % 3 == 0:
            diago[0][color] += 1
        elif (i+j) % 3 == 1:
            diago[1][color] += 1
        else:
            diago[2][color] += 1


# 0列目をcにするときのcにするときの最小コスト
costs = [[0]*c for _ in range(3)]
for i in range(3):
    for j in range(c):
        for k, v in diago[i].items():
            costs[i][j] += D[k][j]*v

INF = 10**18
ans = INF
for trio in itertools.combinations(range(c), 3):
    for color in itertools.permutations(trio, 3):
        cost = sum(costs[i][j] for i, j in enumerate(color))
        if cost < ans:
            ans = cost
print(ans)