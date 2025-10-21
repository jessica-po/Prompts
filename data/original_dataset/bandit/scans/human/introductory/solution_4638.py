n, c = list(map(int, input().split()))
a = [int(ai) for ai in input().split()]
b = [int(bi) for bi in input().split()]

dpa, dpb = [0] * n, [0] * n
dpa[1], dpb[1] = a[0], c + b[0]
for i in range(1, n - 1):
    dpa[i + 1], dpb[i + 1] = min(dpa[i], dpb[i]) + a[i], min(dpa[i] + c, dpb[i]) + b[i]

print(*(min(dpa[i], dpb[i]) for i in range(n)))