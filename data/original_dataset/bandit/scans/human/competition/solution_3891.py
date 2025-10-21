n, m = map(int, input().split())
vert = []
gor = []
for i in range(n):
    s = input()
    for j in range(m):
        if s[j] == 'B':
            vert.append(i)
            gor.append(j)
vert.sort()
gor.sort()
print(vert[len(vert) // 2] + 1, gor[len(gor) // 2] + 1)