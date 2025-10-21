n, k = list(map(int, input().split()))


def get(x):
    if x <= k:
        return x * (x + 1) // 2
    res = k * x - k * (k - 1) // 2
    sz = x - k - 1
    if sz % 2 == 0:
        cnt = sz // 2
        res += (2 + sz) * cnt // 2
    else:
        cnt = sz // 2 + 1
        res += (1 + sz) * cnt // 2
    return res


l = 0
r = 10 ** 18
while r - l > 1:
    m = l + (r - l) // 2
    if get(m) >= n:
        r = m
    else:
        l = m

print(r)