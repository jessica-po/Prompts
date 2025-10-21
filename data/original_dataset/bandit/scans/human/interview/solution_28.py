n = int(input())
t = [1] + [0] * n
b, a = d = [], []
h, s = [], []

for i in range(n):
    f, k = input().split()
    d[int(k)].append(f)

m = len(a)
for i in a:
    if i.isdigit() and i[0] != '0':
        j = int(i)
        if 0 < j <= m:
            t[j] = 1
        elif m < j <= n:
            t[j] = -1
        else:
            s.append(i)
    else:
        s.append(i)
for i in b:
    if i.isdigit() and i[0] != '0':
        j = int(i)
        if m < j <= n:
            t[j] = 1
        elif 0 < j <= m:
            t[j] = -1
        else:
            s.append(i)
    else:
        s.append(i)

x = [j for j in range(1, m + 1) if t[j] < 0]
y = [j for j in range(m + 1, n + 1) if t[j] < 0]

u = [j for j in range(1, m + 1) if not t[j]]
v = [j for j in range(m + 1, n + 1) if not t[j]]

if not s and (x or y):
    s = ['0']
    if y:
        i = y.pop()
        v.append(i)
    else:
        i = x.pop()
        u.append(i)
    h.append(str(i) + ' 0')
    t[i] = 0

while x or y:
    if v and x:
        i = x.pop()
        j = v.pop()
        t[j] = 1
        h.append(str(i) + ' ' + str(j))
        u.append(i)
    else:
        u, v, x, y = v, u, y, x

k = 1
for j in s:
    while t[k] == 1: k += 1
    h.append(j + ' ' + str(k))
    k += 1

d = '\nmove '
print(str(len(h)) + d + d.join(h) if h else 0)