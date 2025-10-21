N, M = [int(n) for n in input().split()]

submit = []
AC = [0] * N
WA = [0] * N

for i in range(M):
    p, s = [n for n in input().split()]
    p = int(p)

    if AC[p-1] == 1:
        continue

    if s == 'AC':
        AC[p-1] = 1
 
    elif s == 'WA':
        WA[p-1] += 1

pen = [x*y for x, y in zip(AC, WA)]

print(sum(AC), sum(pen))