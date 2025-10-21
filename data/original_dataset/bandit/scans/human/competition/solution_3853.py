n = int(input())
t = [tuple(map(int, input().split())) for i in range(n)]

m = max(t)
d = 2 * m[0] + len(bin(m[1])) - 1

t = sorted([i for i in t if 2 * i[0] + len(bin(i[1])) > d])
p, k = t[0][0], t[0][1] - 1

for i in range(1, len(t)):
    p, k = t[i][0], max(t[i][1] - 1, k >> 2 * (t[i][0] - p))

print(p + (len(bin(k)) + 1) // 2 - 1)