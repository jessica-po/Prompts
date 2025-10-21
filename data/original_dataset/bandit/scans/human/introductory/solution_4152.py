from collections import defaultdict
maxn = 2000000000

mk = []
bs = 1

while bs <= maxn:
    mk.append(bs)
    bs *= 2

n = int(input())
ls = [int(i) for i in input().split()]

dic = defaultdict(int)
for i in ls:
    dic[i] += 1

cnt = 0
for i in ls:
    dic[i] -= 1
    flag = False
    for j in mk:
        if dic[j - i] > 0:
            flag = True
            break

    if not flag:
        cnt += 1
    dic[i] += 1

print(cnt)