n, w = list(map(int, input().split()))
Cup = list(map(int, input().split()))
Water = []
for a in Cup:
    Water.append((a + 1) // 2)
res = w - sum(Water)
if res < 0:
    print(-1)
else:
    while res > 0:
        i = Cup.index(max(Cup))
        num = min(res, Cup[i] - Water[i])
        Water[i] += num
        res -= num
        Cup[i] = 0
    s = str(Water[0])
    for c in range(1, len(Water)):
        s += " " + str(Water[c])
    print(s)