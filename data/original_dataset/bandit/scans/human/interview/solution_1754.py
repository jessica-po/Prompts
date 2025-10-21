n, m, k = map(int, input().split())
sch = [0 for i in range(m)]
p = list(map(int, input().split()))
s = list(map(int, input().split()))
c = list(map(int, input().split()))
for i in range(n):
    sch[s[i] - 1] = max(sch[s[i] - 1], p[i])
res = 0
for i in c:
    i -= 1
    res += p[i] != sch[s[i] - 1]
print(res)