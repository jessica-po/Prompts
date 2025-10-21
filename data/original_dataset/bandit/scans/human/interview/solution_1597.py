import sys

SIGMA = 26

nodes = []
pairs = []
res = 0

class Node:
    def __init__(self):
        self.ch = {}
        self.a = []
        self.b = []
        self.d = 0

    def add(self, s, i):
        t = self
        for c in s:
            v = ord(c) - ord('a')
            if not v in t.ch:
                t.ch[v] = Node()
                t.ch[v].d = t.d + 1
                nodes.append(t.ch[v])
            t = t.ch[v]
        t.a.append(i)

    def inc(self, s, i):
        t = self
        for c in s:
            v = ord(c) - ord('a')
            if not v in t.ch:
                break
            t = t.ch[v]
        t.b.append(i)

    def solve(self):
        nonlocal pairs
        nonlocal res
        for i in range(SIGMA):
            if i in self.ch:
                self.a.extend(self.ch[i].a)
                self.b.extend(self.ch[i].b)
        k = min(len(self.a), len(self.b))
        for i in range(k):
            pairs.append(str(self.a[-1]) + ' ' + str(self.b[-1]))
            self.a.pop()
            self.b.pop()
            res += self.d
        return res

sys.setrecursionlimit(2000000)
_input = sys.stdin.readlines()
_input = [s[:-1] for s in _input]
N = int(_input[0])
A = _input[1 : N + 1]
B = _input[N + 1 :]
T = Node()
nodes.append(T)
for i, s in enumerate(A):
    T.add(s, i + 1)
for i, s in enumerate(B):
    T.inc(s, i + 1)
for n in reversed(nodes):
    n.solve()
print(res)
print('\n'.join(pairs))