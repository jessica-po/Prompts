import bisect

_ = input()
a = sorted(map(int, input().split()))

n = a[-1]

m = n / 2
b = bisect.bisect(a, m)
s = a[b - 1]
t = a[b]
if m - s <= t - m:
    print(n, s)
else:
    print(n, t)