#Simple non-optimized class of matrices. Used with small dense matrices.
import functools
import itertools
import math

class NotAMatrixError(Exception):
    pass

class MatrixSizeError(Exception):
    def __init__(self, s1, s2):
        print('sizes do not match : ', s1, ', ', s2)

class NotSquareError(Exception):
    pass

class Matrix(list):
    def __init__(self, L):
        if type(L) == type(self):
            self = L
            return
        n = len(L)
        m = len(L[0])
        for i in range(n):
            if len(L[i]) != m:
                raise NotAMatrixError()
        list.__init__(self, L)
        self.n = n
        self.m = m
        self.degrees = []
    def check_size(self, M, mode):
        n, m = len(M), len(M[0])
        for i in range(n):
            if len(M[i]) != m:
                raise NotAMatrixError()
        
        if mode == 'add' and (self.n != n or self.m != m):
            raise MatrixSizeError((self.n, self.m), (n,m))
        if mode == 'lul' and self.m != n:
            print(self.m, n, self.m != n)
            raise MatrixSizeError((self.n, self.m), (n,m))
    def __add__(self, M):
        self.check_size(M, mode = 'add')
        return Matrix([[self[i][j]+M[i][j] for j in range(self.m)]for i in range(self.n)])
    def __iadd__(self, M):
        self.check_size(M, mode = 'add')
        for i in range(self.n):
            for j in range(self,m):
                self[i][j] += M[i][j]
    def __mul__(self, M):
        self.check_size(M, mode = 'mul')
        l = len(M[0])
        return Matrix([[sum(self[i][k]*M[k][j] for k in range(self.m))
                 for j in range(l)] for i in range(self.n)])
    def issquare(self):
        return self.n == self.m
    def primary(self):
        if self.n != self.m:
            raise NotSquareError()
        return Matrix([[int(i==j) for j in range(self.m)] for i in range(self.n)])
    def __pow__(self, n):
        if self.n != self.m:
            raise NotSquareError()
        if n == 0:
            return self.primary()
        elif n == 1:
            return self
        if len(self.degrees) == 0:
            self.degrees.append(self*self)
        for i in range(n.bit_length() - len(self.degrees) - 1):
            self.degrees.append(self.degrees[-1] * self.degrees[-1])
        s = [(n>>i)&1 for i in range(1,n.bit_length())]
        res = functools.reduce(lambda x,y:x*y, itertools.compress(self.degrees, s))
        return res*self if n%2 else res 
    def drop_degrees(self):
        self.degrees.clear()

class Remainder(int):
    def __new__(self, n, p):
        obj = int.__new__(self, n%p)
        obj.p = p
        return obj
    def __mul__(self, m): return Remainder(int.__mul__(self, m), self.p)
    def __add__(self, m): return Remainder(int.__add__(self, m), self.p)
    def __sub__(self, m): return Remainder(int.__sub__(self, m), self.p)
    def __rmul__(self, m): return Remainder(int.__rmul__(self, m), self.p)
    def __radd__(self, m): return Remainder(int.__radd__(self, m), self.p)
    def __rsub__(self, m): return Remainder(int.__rsub__(self, m), self.p)
    def __neg__(self): return Remainder(int.__neg__(self), self.p)
    def __pow__(self, m): return Remainder(int.__pow__(self, m, self.p), self.p)

def solve(n, sx, sy, dx, dy, t):
    o, l, j = Remainder(0, n), Remainder(1, n), Remainder(2, n)
    N = [[j, l, l, o, l, o],
         [l, j, o, l, l, o],
         [l, l, l, o, l, o],
         [l, l, o, l, l, o],
         [o, o, o, o, l, l],
         [o, o, o, o, o, l]]
    M = Matrix(N)
    sx, sy, dx, dy = [Remainder(x, n) for x in [sx, sy, dx, dy]]
    v = Matrix([[sx], [sy], [dx], [dy], [o], [l]])
    return M ** t * v

n, sx, sy, dx, dy, t = [int(x) for x in input().split()]
ans = solve(n, sx, sy, dx, dy, t)
print(int(ans[0][0] - 1) + 1, int(ans[1][0] - 1) + 1)