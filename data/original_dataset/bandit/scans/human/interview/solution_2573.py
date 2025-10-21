import collections
import math
n, k, m = [int(i) for i in input().split()]
l = math.ceil((math.log(2*n) / math.log(2)))
p = 2 ** l
# print(p)
memo = [0] * (2 * p)
allres = [0] * (2 * p)

exist = set()
for _i in range(m):
    x, y = [int(i) for i in input().split()]
    l = abs(x - k) + y
    index = l + p
    if (x, y) in exist:
        exist.remove((x, y))
        while index != 0:
            memo[index] -= 1
            index = index // 2
    else:
        exist.add((x, y))
        while index != 0:
            memo[index] += 1
            index = index // 2
    index = (l + p) // 2
    allres[l+p] = l + memo[l + p] - 1
    if memo[l + p] == 0:
        allres[l+p] = 0
    while index != 0:
        allres[index] = max(allres[index * 2] + memo[index * 2 + 1], allres[index * 2 + 1])
        index = index // 2
    # print('i', _i + 1, exist, allres, memo)
    
    print(max(allres[1] - n, 0))