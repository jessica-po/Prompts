class UnionFind:
    def __init__(self, n):
        self.par = [i for i in range(n + 1)]
        self.rank = [0] * (n + 1)
        self.size = [1] * (n + 1)

    def find(self, x):
        if self.par[x] == x:
            return x
        else:
            self.par[x] = self.find(self.par[x])
            return self.par[x]

    def same_check(self, x, y):
        return self.find(x) == self.find(y)

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if self.rank[x] < self.rank[y]:
            if self.same_check(x, y) != True:
                self.size[y] += self.size[x]
                self.size[x] = 0
            self.par[x] = y
        else:
            if self.same_check(x, y) != True:
                self.size[x] += self.size[y]
                self.size[y] = 0
            self.par[y] = x
            if self.rank[x] == self.rank[y]:
                self.rank[x] += 1

    def siz(self, x):
        x = self.find(x)
        return self.size[x]


N = int(input())
UF = UnionFind(N)
X = []
Y = []
Branch = []
for i in range(N):
    x, y = list(map(int, input().split()))
    X.append((x, i))
    Y.append((y, i))
X.sort()
Y.sort()
for X1, X2 in zip(X, X[1:]):
    Branch.append((X2[0] - X1[0], X1[1], X2[1]))
for Y1, Y2 in zip(Y, Y[1:]):
    Branch.append((Y2[0] - Y1[0], Y1[1], Y2[1]))
Branch.sort()

# 負のとき size, 非負のとき parent
par = [-1] * N
ans = 0
for c, a, b in Branch:
    if N <= 1:
        break
    if not UF.same_check(a, b):
        UF.union(a, b)
        ans += c
        N -= 1

print(ans)