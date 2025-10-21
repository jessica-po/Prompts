n = int(input())
l = tuple(map(int, input().split()))

a = []
for i in range(n - 1):
    a.append(abs(l[i] - l[i + 1]))

ev = [(a[i] if i % 2 == 0 else -a[i]) for i in range(n - 1)]
od = [-i for i in ev]
od[0] = 0

dp = [ev[0]]
st = ["ev"]

# print(a)
# print(ev)
# print(od)

vmax = dp[0]

evsum = evans = 0
odsum = odans = 0

for i in range(0, n - 1):
    evsum += ev[i]
    odsum += od[i]
    evans = max(evsum, evans)
    odans = max(odsum, odans)
    if evsum < 0 and i % 2 == 1:
        evsum = 0
    if odsum < 0 and i % 2 == 0:
        odsum = 0

# print(evans, odans)

print(max(evans, odans))