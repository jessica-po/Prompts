n = int(input())
a = [tuple(map(int, input().split())) for _ in range(n)]
s = {a[q]: q+1 for q in range(n)}
a.sort()
q, q1 = 0, 1
d, d1, d2 = [[[a[0]]]], [], []
while q1 < n:
    while q1 < n and a[q][0] == a[q1][0]:
        while q1 < n and a[q][1] == a[q1][1]:
            d[-1][-1].append(a[q1])
            q1 += 1
        if q1 < n and a[q][0] == a[q1][0]:
            d[-1].append([a[q1]])
            q = q1
            q1 += 1
    if q1 < n:
        d.append([[a[q1]]])
        q = q1
        q1 += 1
for q in range(len(d)):
    for q1 in range(len(d[q])):
        for q2 in range(1, len(d[q][q1]), 2):
            print(s[d[q][q1][q2-1]], s[d[q][q1][q2]])
        if len(d[q][q1]) % 2 == 1:
            d[q][q1] = d[q][q1][-1]
        else:
            d[q][q1] = -1
for q in range(len(d)):
    d1.append([])
    for q1 in range(len(d[q])):
        if d[q][q1] != -1:
            d1[-1].append(d[q][q1])
for q in range(len(d1)):
    for q1 in range(1, len(d1[q]), 2):
        print(s[d1[q][q1-1]], s[d1[q][q1]])
    if len(d1[q]) % 2 == 1:
        d2.append(d1[q][-1])
for q in range(1, len(d2), 2):
    print(s[d2[q-1]], s[d2[q]])