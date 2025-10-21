def sum_zeroth(arr):
    res = 0
    for elem in arr:
        res += elem[0]
    return res

n, a, b, k = list(map(int, input().split()))
data = input()
dist = []
pp = 0

last = 0
for i in range(n):
    if data[i] == '1':
        dist.append((last, i))
        pp += (i - last) // b
        last = i + 1

dist.append((last, n))
pp += (n - last) // b
pos = []
minp = pp - a + 1
fnd = False

for elem in dist:
    cur = elem[0] - 1
    while (cur + b) < elem[1]:
        cur += b
        pos.append(cur + 1)
        if len(pos) == minp:
            fnd = True
            break
    if fnd:
        break

print(minp)
print(' '.join(map(str, pos)))