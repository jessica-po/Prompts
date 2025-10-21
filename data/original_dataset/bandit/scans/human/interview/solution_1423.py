n, l, r = list(map(int, input().split()))
read = lambda: list(map(int, input().split()))
a = list(read())
p = list(read())
d = [(a[i], p[i], i) for i in range(n)]
d.sort(key = lambda x: x[1])
cur = l - d[0][0]
b = [0] * n
for i in range(n):
    ind = d[i][2]
    b[ind] = a[ind] + cur
    if b[ind] < l:
        cur = l - a[ind]
        b[ind] = l
    cur += 1
if max(b) > r: 
    print(-1)
    return
print(' '.join(map(str, b)))