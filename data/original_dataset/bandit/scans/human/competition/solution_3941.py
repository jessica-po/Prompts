import sys
import collections

n, m = list(map(int, input().split()))

r = tuple(map(int, input().split()))

controls = [tuple(map(int, input().split()))[1:] for i in range(m)]


class DSU:

    def __init__(self):
        self.parent = None
        self.has_zero = False
        self.has_one = False
        self.size = 1
        self.doors = []

    def get_root(self):
        if self.parent is None:
            return self
        self.parent = self.parent.get_root()
        return self.parent

    def unite(self, s):
        r1 = self.get_root()
        r2 = s.get_root()

        if r1 is r2:
            return r1

        if r1.size < r2.size:
            r1, r2 = r2, r1

        r2.parent = r1
        r1.size += r2.size
        r1.has_zero = r1.has_zero or r2.has_zero
        r1.has_one = r1.has_one or r2.has_one

        return r1

door_dsus = [[] for i in range(n)]
for doors in controls:
    n = DSU()
    for door in doors:
        n.doors.append(door - 1)

        door_dsus[door - 1].append(n)
        if r[door - 1]:
            n.has_one = True
        if not r[door - 1]:
            n.has_zero = True

for door, is_open in enumerate(r):
    n1, n2 = door_dsus[door]

    if is_open:
         n1.unite(n2)

G = {}
for door, is_open in enumerate(r):
    if is_open:
        continue

    n1, n2 = door_dsus[door]
    if n1.get_root() is n2.get_root():
        print("NO")
        return

    G.setdefault(n1.get_root(), set()).add(n2.get_root())
    G.setdefault(n2.get_root(), set()).add(n1.get_root())

color = {}

for v in list(G.keys()):
    if v in color:
        continue

    color[v] = False
    q = collections.deque([v])
    while q:
        v = q.popleft()
        c = color[v]
        for adj_v in G[v]:
            if adj_v in color:
                if color[adj_v] != (not c):
                    print("NO")
                    return
            else:
                color[adj_v] = not c
                q.append(adj_v)

print("YES")