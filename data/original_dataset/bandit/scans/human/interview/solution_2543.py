def read(): return list(map(int, input().split(' ')))
n, m, q = read()
aa = read()
bb = read()
reqs = [read() for _ in range(q)]

asum = 0
bsum = 0
for i, (a, b) in enumerate(zip(aa, bb)):
    asum += a if i % 2 == 0 else -a
    bsum += b if i % 2 == 0 else -b

bpos = [bsum]
for i in range(len(aa), len(bb)):
    b = bb[i]

    rempos = i - len(aa)
    bsum += b if i % 2 == 0 else -b
    bsum -= bb[rempos] if rempos % 2 == 0 else -bb[rempos]
    bpos += [bsum if rempos % 2 == 1 else -bsum]

bpos = sorted(set(bpos))

def closest(arr, value):
    l = 0
    r = len(arr)
    while l + 1 < r:
        m = (l + r) // 2
        if arr[m] <= value:
            l = m
        else:
            r = m
        
    res = arr[l]
    if l + 1 < len(arr) and abs(arr[l + 1] - value) < abs(arr[l] - value):
        res = arr[l + 1]
    return res

print(abs(asum - closest(bpos, asum)))
for req in reqs:
    l, r, x = req
    l -= 1
    if (r - l) % 2 != 0:
        asum += x if l % 2 == 0 else -x
    print(abs(asum - closest(bpos, asum)))