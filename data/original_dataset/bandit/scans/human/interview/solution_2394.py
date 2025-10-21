"""
#If FastIO not needed, used this and don't forget to strip
#import sys, math
#input = sys.stdin.readline
"""

import os
import sys
from io import BytesIO, IOBase
import heapq as h 
from bisect import bisect_left, bisect_right

from types import GeneratorType
BUFSIZE = 8192
class FastIO(IOBase):
    newlines = 0
 
    def __init__(self, file):
        import os
        self.os = os
        self._fd = file.fileno()
        self.buffer = BytesIO()
        self.writable = "x" in file.mode or "r" not in file.mode
        self.write = self.buffer.write if self.writable else None
 
    def read(self):
        while True:
            b = self.os.read(self._fd, max(self.os.fstat(self._fd).st_size, BUFSIZE))
            if not b:
                break
            ptr = self.buffer.tell()
            self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
        self.newlines = 0
        return self.buffer.read()
 
    def readline(self):
        while self.newlines == 0:
            b = self.os.read(self._fd, max(self.os.fstat(self._fd).st_size, BUFSIZE))
            self.newlines = b.count(b"\n") + (not b)
            ptr = self.buffer.tell()
            self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
        self.newlines -= 1
        return self.buffer.readline()
 
    def flush(self):
        if self.writable:
            self.os.write(self._fd, self.buffer.getvalue())
            self.buffer.truncate(0), self.buffer.seek(0)
 
 
class IOWrapper(IOBase):
    def __init__(self, file):
        self.buffer = FastIO(file)
        self.flush = self.buffer.flush
        self.writable = self.buffer.writable
        self.write = lambda s: self.buffer.write(s.encode("ascii"))
        self.read = lambda: self.buffer.read().decode("ascii")
        self.readline = lambda: self.buffer.readline().decode("ascii")
 
 
sys.stdin, sys.stdout = IOWrapper(sys.stdin), IOWrapper(sys.stdout)
input = lambda: sys.stdin.readline().rstrip("\r\n")

from collections import defaultdict as dd, deque as dq, Counter as dc
import math, string


def getInts():
    return [int(s) for s in input().split()]

def getInt():
    return int(input())

def getStrs():
    return [s for s in input().split()]

def getStr():
    return input()

def listStr():
    return list(input())

def getMat(n):
    return [getInts() for _ in range(n)]

MOD = 10**9+7


"""
Each edge goes from parent U to child V
Edge appears on S_V * (N - S_V) paths

For each path of length L, (L + (-L)%K)/K


L%K 0, 1, 2, 3, 4
(K - L%K)%K K K-1 K-2 ...
0 K-1 K-2 ...

"""
def bootstrap(f, stack=[]):
    def wrappedfunc(*args, **kwargs):
        if stack:
            return f(*args, **kwargs)
        else:
            to = f(*args, **kwargs)
            while True:
                if type(to) is GeneratorType:
                    stack.append(to)
                    to = next(to)
                else:
                    stack.pop()
                    if not stack:
                        break
                    to = stack[-1].send(to)
            return to
    return wrappedfunc

def solve():
    N, K = getInts()
    graph = dd(set)
    for i in range(N-1):
        A, B = getInts()
        graph[A].add(B)
        graph[B].add(A)
    dp_count = [[0 for j in range(5)] for i in range(N+1)]
    dp_total = [0 for j in range(N+1)]
    nonlocal ans
    ans = 0
    @bootstrap
    def dfs(node,parent,depth):
        nonlocal ans
        dp_count[node][depth % K] = 1
        dp_total[node] = 1
        for neigh in graph[node]:
            if neigh != parent:
                yield dfs(neigh,node,depth+1)
                for i in range(K):
                    for j in range(K):
                        diff = (i+j-2*depth)%K
                        req = (-diff)%K
                        ans += req * dp_count[node][i] * dp_count[neigh][j]
                for i in range(K):
                    dp_count[node][i] += dp_count[neigh][i]
                dp_total[node] += dp_total[neigh]
        ans += dp_total[node] * (N - dp_total[node])
        yield
    dfs(1,-1,0)
    return ans//K
    
    
print(solve())