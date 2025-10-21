# ひっくりかえすのかとお保ったら180度反転だった
n = int(input())
d = []
for _ in range(n):
    s = list(input())
    d.append(s)

d = sorted(d, key=lambda dd: len(dd), reverse=True)
base = {}
for c in d[0]:
    if c not in base:
        base[c] = 1
    else:
        base[c] += 1

for s in d[1:]:
    tmp = {}
    for c in s:
        if c not in tmp:
            tmp[c] = 1
        else:
            tmp[c] += 1
    for k, v in base.items():
        if k in tmp and base[k] >= 1:
            base[k] = min(base[k], tmp[k])
        else:
            base[k] = -1
ans = []
for k, v in base.items():
    if v > 0:
        ans.append(k * v)
ans = sorted(ans)
ans = "".join(ans)
print(ans)