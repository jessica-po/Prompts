import sys

answer = 1
z = True
primes = []
for i in range (2, 5 * 10 ** 2):
    v = True
    for p in primes:
        if i % p == 0:
            v = False
    if v == True:
        primes.append(i)

n = int(sys.stdin.readline().strip())
a = list(map(int, sys.stdin.readline().strip().split()))
if sum(a) == n:
    z = False
for i in range (0, n):
    x = a[i]
    a[i] = []
    for p in primes:
        if x % p == 0:
            a[i].append([p, 1])
            x = x // p
            while x % p == 0:
                x = x // p
    if x != 1:
        a[i].append([x, 1])

neighbours = [[] for i in range (0, n)]
for i in range (0, n - 1):
    line = sys.stdin.readline().strip().split()
    neighbours[int(line[0]) - 1].append(int(line[1]) - 1)
    neighbours[int(line[1]) - 1].append(int(line[0]) - 1)

leaves = []
for i in range (0, n):
    if len(neighbours[i]) == 1:
        leaves.append(i)


while len(leaves) > 1:
    x = leaves.pop()
    y = neighbours[x][0]
    neighbours[y].remove(x)
    if len(neighbours[y]) == 1:
        leaves.append(y)
    for p in a[x]:
        for q in a[y]:
            if p[0] == q[0]:
                answer = max([answer, p[1] + q[1]])
                q[1] = max([q[1],p[1]+1])


if z == False:
    print(0)
else:
    print(answer)