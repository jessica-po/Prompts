a, b, c = map(int, input().split())
d = 1073741824
p = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
t = [{} for i in range(101)]
ans = {}
for i in p:
    j = i
    m = 1
    while j < 101:
        for k in range(j, 101, j):
            t[k][i] = m
        j = j * i
        m += 1
s = 0
for i in range(1, a + 1):
    for j in range(1, b + 1):
        q = {}
        for x in t[i].keys() | t[j].keys():
            q[x] = t[i].get(x, 0) + t[j].get(x, 0)
        ij = i * j
        for k in range(1, c + 1):
            ijk = ij * k
            if ijk in ans: s += ans[ijk]
            else:
                y = 1
                for x in q.keys() | t[k].keys():
                    y = y * (q.get(x, 0) + t[k].get(x, 0) + 1)
                ans[ijk] = y
                s += y

print(s)