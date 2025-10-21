n = int(input())
l = []
for i in range(n + 1):
    l.append(0)
for i in range(2, n + 1):
    for j in range(i * 2, n + 1, i):
        l[j] = i
l.sort()
for i in range(2, n + 1):
    if l[i] == 0:
        print(1, end=" ")
    else:
        print(l[i], end=" ")