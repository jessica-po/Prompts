class UnionFindVerSize():
    def __init__(self, N):
        self._parent = [n for n in range(0, N)]
        self._size = [1] * N
        self.group = N

    def find_root(self, x):
        if self._parent[x] == x: return x
        self._parent[x] = self.find_root(self._parent[x])
        stack = [x]
        while self._parent[stack[-1]]!=stack[-1]:
            stack.append(self._parent[stack[-1]])
        for v in stack:
            self._parent[v] = stack[-1]
        return self._parent[x]

    def unite(self, x, y):
        gx = self.find_root(x)
        gy = self.find_root(y)
        if gx == gy: return

        self.group -= 1

        if self._size[gx] < self._size[gy]:
            self._parent[gx] = gy
            self._size[gy] += self._size[gx]
        else:
            self._parent[gy] = gx
            self._size[gx] += self._size[gy]

    def get_size(self, x):
        return self._size[self.find_root(x)]

    def is_same_group(self, x, y):
        return self.find_root(x) == self.find_root(y)

import sys

input = sys.stdin.readline

for _ in range(int(input())):
    N,M = list(map(int,input().split()))
    uf = UnionFindVerSize(N)
    for _ in range(M):
        a,b = list(map(int,input().split()))
        uf.unite(a-1,b-1)

    if N%2==1:
        all = N*(N-1)//2-M
        if all%2==0:
            print("Second")
        else:
            print("First")
    else:
        all = N*(N-1)//2-M
        s1 = uf.get_size(0)
        sN = uf.get_size(N-1)
        if s1%2==sN%2:
            if s1%2==0:
                if all%2==0:
                    print("Second")
                else:
                    print("First")
            else:
                if all%2==1:
                    print("Second")
                else:
                    print("First")
        else:
            print("First")

#odd,even->even,even first
#odd,even->odd,odd first
#odd,odd->even,even second
#odd,odd->odd,odd first
#even,even->even,even first
#even,even->odd,odd second