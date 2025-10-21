n, m, k = list(map(int, input().split()))
x, s = list(map(int, input().split()))
t = list(map(int, input().split()))
pr = list(map(int, input().split()))
t2 = list(map(int, input().split()))
pr2 = list(map(int, input().split()))
mass1 = []
minans = 10**20
for i in range(m):
    mass1.append((pr[i], t[i]))
mass1.sort()
mass1 = [(0, x)] + mass1
pr2 = [0] + pr2
t2 = [0] + t2
uk1 = len(mass1) - 1
uk2 = 0
maxw = 0
for uk1 in range(len(mass1) - 1, -1, -1):
    if (s < mass1[uk1][0]):
        continue
    while (uk2 < len(pr2) and mass1[uk1][0] + pr2[uk2] <= s):
        maxw = max(maxw, t2[uk2])
        uk2 += 1
    uk2 -= 1
    minans = min(minans, (n - maxw) * mass1[uk1][1])
print(minans)