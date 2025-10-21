from collections import deque

__author__ = 'asmn'

n = int(input())
end = tuple(sorted(map(lambda x: int(x) - 1, input().split())))
st = (0, 1, 2)
mat = [input() for i in range(n)]
v = set([st])
path = {}
dist = {st: 0}
queue = deque([st])

while end not in v and len(queue) > 0:
    p = queue.popleft()

    for x in range(-2, 1):
        p1, p2, p3 = p[x], p[x + 1], p[x + 2]
        for i in range(n):
            if i not in (p1, p2, p3) and mat[i][p3] == mat[p1][p2]:
                np = tuple(sorted((p1, p2, i)))
                if np not in v:
                    v.add(np)
                    queue.append(np)
                    path[np] = p
                    dist[np] = dist[p] + 1


def pathinfo(fr, to):
    return str((set(fr) - set(to)).pop() + 1) + ' ' + str((set(to) - set(fr)).pop() + 1)


if end not in dist:
    print(-1)
    return

print(dist[end])
while end in path:
    print(pathinfo(end, path[end]))
    end = path[end]