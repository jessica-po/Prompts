"""
Codeforces Contest Good Bye 2014 Contest Problem B

Author  : chaotic_iak
Language: Python 3.4.2
"""

################################################### SOLUTION

def main():
    n, = read()
    p = read()
    dsu = DSU()
    for i in range(n):
        a = read(0)
        dsu.make()
        for j in range(i):
            if a[j] == "1":
                dsu.union(j, i)
    used = [0] * n
    res = [0] * n
    for i in range(n):
        if not used[i]:
            pr = dsu.find(i)
            indices = []
            elements = []
            for j in range(n):
                if dsu.find(j) == pr:
                    used[j] = 1
                    indices.append(j)
                    elements.append(p[j])
            elements.sort()
            for i,e in zip(indices, elements):
                res[i] = e
    write(res)

#################################################### HELPERS

class DSU(object):
    """
    Implements disjoint-set data structure as disjoint-set forest, with {0,1,...,n-1} as elements.

    Methods:
    make(): add a new element and returns its index
    find(x): return representative of x
    union(x, y): merge the sets containing x and y

    Not to be used publicly:
    _parent: a list of ints for the parent of each vertex, used internally; call find instead
    _rank: a list of ints for the rank of trees, ensuring trees are binary and hence O(lg n) worst case
    __init__(): called when initialization, initialize DSU to be empty
    __str__(): return a readable string description of the DSU; meant to be printed while debugging
    """

    def __init__(self):
        self._parent = []
        self._rank = []

    def make(self):
        i = len(self._parent)
        self._parent.append(i)
        self._rank.append(0)
        return i

    def find(self, x):
        if self._parent[x] != x:
            self._parent[x] = self.find(self._parent[x])
        return self._parent[x]

    def union(self, x, y):
        xr = self.find(x)
        yr = self.find(y)
        if xr == yr: return
        if self._rank[xr] < self._rank[yr]:
            self._parent[xr] = yr
        elif self._rank[yr] < self._rank[xr]:
            self._parent[yr] = xr
        else:
            self._parent[yr] = xr
            self._rank[xr] += 1

    def __str__(self):
        s = "DSU\n"
        for i in range(len(self._parent)):
            s += str(i) + " in set " + str(self.find(i)) + " with rank " + str(self._rank[self.find(i)]) + "\n"
        return s

def read(mode=2):
    # 0: String
    # 1: List of strings
    # 2: List of integers
    inputs = input().strip()
    if mode == 0: return inputs
    if mode == 1: return inputs.split()
    if mode == 2: return list(map(int, inputs.split()))

def write(s="\n"):
    if s is None: s = ""
    if isinstance(s, list): s = " ".join(map(str, s))
    s = str(s)
    print(s, end="")

write(main())