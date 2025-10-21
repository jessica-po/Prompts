n = int(input())
ls = list(map(int, input().split()))

msf = 0
res = []
for e in ls:
    v = msf + e
    msf = max(msf, v)
    res.append(v)

for e in res:
    print(e, end=' ')