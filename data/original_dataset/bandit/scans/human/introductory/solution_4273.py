#!/usr/bin/env python3
import itertools

n = int(input())


data = [[] for i in range(5)]
# print(data)
for i in range(n):
    tmp = str(input())
    if tmp[0] == "M":
        data[0].append(tmp)
    elif tmp[0] == "A":
        data[1].append(tmp)
    elif tmp[0] == "R":
        data[2].append(tmp)
    elif tmp[0] == "C":
        data[3].append(tmp)
    elif tmp[0] == "H":
        data[4].append(tmp)

ans = 0
for i, j, k in itertools.combinations([0, 1, 2, 3, 4], 3):
    ans += len(data[i])*len(data[j])*len(data[k])
print(ans)