import sys


def count(n, k, field):
    blank = 0
    cnt = [[0] * (n - k + 1) for _ in range(n)]
    for i, row in enumerate(field):
        l = row.find('B')
        r = row.rfind('B')
        if l == r == -1:
            blank += 1
            continue
        if r - l + 1 > k:
            continue
        kl = max(0, r - k + 1)
        kr = min(l + 1, n - k + 1)
        cnt[i][kl:kr] = [1] * (kr - kl)

    acc = [[0] * (n - k + 1) for _ in range(n - k + 1)]
    t_cnt = list(zip(*cnt))
    for i, col in enumerate(t_cnt):
        aci = acc[i]
        tmp = sum(col[n - k:])
        aci[n - k] = tmp
        for j in range(n - k - 1, -1, -1):
            tmp += col[j]
            tmp -= col[j + k]
            aci[j] = tmp

    return blank, acc


n, k = list(map(int, input().split()))
field = [line.strip() for line in sys.stdin]
bh, hor = count(n, k, field)
t_field = [''.join(col) for col in zip(*field)]
bv, t_var = count(n, k, t_field)
var = list(zip(*t_var))

print(bh + bv + max(h + v for (rh, rv) in zip(hor, var) for (h, v) in zip(rh, rv)))