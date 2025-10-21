n, s = [int(x) for x in input().split()]

ts = []
for _ in range(n):
    h, m = [int(x) for x in input().split()]
    ts.append(h * 60 + m)

if ts[0] >= s + 1:
    print(0, 0)
    return

diffs =  [y - x for x, y in zip(ts, ts[1:])]

for i, diff in enumerate(diffs):
    if diff >= 2 * s + 2:
        break
else:
    i = len(ts) - 1

t = ts[i] + s + 1
print(t // 60, t % 60)