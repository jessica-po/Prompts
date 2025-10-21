import sys


n = int(input())
a = [int(t) for t in input().split(' ')]
mx = [[] for _ in range(n)]

lines = sys.stdin.readlines()
for i in range(n-1):
    v1, v2 = (int(t) - 1 for t in lines[i].split(' '))
    mx[v1].append(v2)
    mx[v2].append(v1)

count = [[0, 0] for _ in range(n)]

total = [a.count(1), a.count(2)]
answer = 0

OBSERVE = 0
CHECK = 1

stack = [(OBSERVE, 0, -1)]
while len(stack):
    state, v, from_ = stack.pop()
    if state == OBSERVE:
        stack.append((CHECK, v, from_))
        for nv in mx[v]:
            if nv != from_:
                stack.append((OBSERVE, nv, v))
    else:
        for nv in mx[v]:
            if nv != from_:
                if count[nv][0] == total[0] and count[nv][1] == 0 or count[nv][1] == total[1] and count[nv][0] == 0:
                    answer += 1
                count[v][0] += count[nv][0]
                count[v][1] += count[nv][1]

        if a[v] != 0:
            count[v][a[v]-1] += 1

print(answer)