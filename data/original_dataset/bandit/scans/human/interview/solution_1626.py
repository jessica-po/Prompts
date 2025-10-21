import math

n, k = [int(x) for x in input().split()]

a = [int(x) for x in input().split()]
b = [int(x) for x in input().split()]

c = 1
for i in range(n // k):
    count = (10 ** k - 1) // a[i] + 1
    mmin = b[i] * (10 ** (k-1))
    mmax = (b[i] + 1) * (10 ** (k-1)) - 1
    mcount = mmax // a[i] - math.ceil(mmin / a[i]) + 1
    c = (c * (count - mcount)) % ((10 ** 9) + 7)

print(c)