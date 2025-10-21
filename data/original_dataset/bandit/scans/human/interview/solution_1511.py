n, m, k = list(map(int, input().split()))
deadstep = [0] * (n+1)
badmem = [False] * (k+1)
a = [0] * (n+1)
for i in range(1, n+1):
    a[i] = [0] + list(map(int, input().split()))
for step in range(1, m+1):
    t = [0] * (k+1)
    for i in range(1, n+1):
        if deadstep[i] == 0 and a[i][step] != 0:
            t[a[i][step]] += 1
    for j in range(1, k+1):
        if t[j] > 1:
            badmem[j] = True
    for i in range(1, n+1):
        if deadstep[i] == 0 and badmem[a[i][step]]:
            deadstep[i] = step
for i in range(1, n+1):
    print(deadstep[i])