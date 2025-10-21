from collections import defaultdict,deque
import sys,heapq,bisect,math,itertools,string,queue,copy,time
sys.setrecursionlimit(10**8)
INF = float('inf')
mod = 10**9+7
eps = 10**-7
def inp(): return int(sys.stdin.readline())
def inpl(): return list(map(int, sys.stdin.readline().split()))
def inpl_str(): return list(sys.stdin.readline().split())


def gcd(a,b):
	while b:
		a,b = b, a%b
	return a

T = inp()
for _ in range(T):
    a,b,k = inpl()
    a,b = min(a,b), max(a,b)

    n = gcd(a,b)
    # while n < b:
    #     n += a
    #     cnt += 1
    cnt = -((n-b)//a)


    if cnt >= k:
        print("REBEL")
    else:
        print("OBEY")