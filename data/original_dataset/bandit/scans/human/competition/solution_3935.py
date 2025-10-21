n = int(input())
b = [int(x) for x in input().strip().split()]

result = {}

for x in b:
    tmp = x
    cnt = 0
    while tmp & 1 == 0:
        cnt += 1
        tmp >>= 1
    if cnt not in result:
        result[cnt] = []
    result[cnt].append(x)

res1 = max([len(result[x]) for x in result])
print(n - res1)
if n == res1:
    return

res2 = None
for x in result:
    if len(result[x]) == res1:
        res2 = x
        break

res3 = []
for x in result:
    if x != res2:
        for y in result[x]:
            res3.append(str(y))

print(' '.join(res3))