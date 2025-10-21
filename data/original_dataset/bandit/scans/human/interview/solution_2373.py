import sys
input = sys.stdin.readline
from collections import deque


def read():
    N = int(input().strip())
    P = list(map(int, input().strip().split()))
    return N, P


def solve(N, P):
    ans = 0
    p = deque(P)
    q = deque()
    q.append(p.popleft())
    for i in range(1, N):
        if i == q[-1]:
            c = q.pop()
            q.append(p.popleft())
            q.append(c)
            ans += 1
        else:
            q.append(p.popleft())
    if q[-1] == N:
        c = q.pop()
        d = q.pop()
        q.append(c)
        q.append(d)
        ans += 1
    return ans


def __starting_point():
    inputs = read()
    print((solve(*inputs)))

__starting_point()