n, m = list(map(int, input().split()))
a = list(map(int, input().split()))
b = list(map(int, input().split()))

possible = [[] for i in range(n)]

for i in range(n):
    for j in range(m):
        possible[i].append(a[i] & b[j])

import sys
for answer in range(2 ** 9):
    answer_flag = 1
    for i in range(n):
        flag = 0
        for x in possible[i]:
            if answer | x == answer:
                flag = 1
                break
        if flag == 0:
            answer_flag = 0
            break
    if answer_flag:
        print(answer)
        return