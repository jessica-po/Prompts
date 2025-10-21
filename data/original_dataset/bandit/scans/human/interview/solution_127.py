n, f = list(map(int, input().split(' ')))
res = 0
wow = []
for a0 in range(n):
    k, l = list(map(int, input().split(' ')))
    res += min(k, l)
    wow.append(min(2*k, l) - min(k, l))
wow = sorted(wow)
i = len(wow)-1
for a0 in range(f):
    res += wow[i]
    i -= 1
print(res)