import math
from math import gcd,pi,sqrt
INF = float("inf")
MOD = 10**9 + 7

import sys
sys.setrecursionlimit(10**6)
import itertools
import bisect
from collections import Counter,deque
def i_input(): return int(input())
def i_map(): return map(int, input().split())
def i_list(): return list(i_map())
def i_row(N): return [i_input() for _ in range(N)]
def i_row_list(N): return [i_list() for _ in range(N)]
def s_input(): return input()
def s_map(): return input().split()
def s_list(): return list(s_map())
def s_row(N): return [s_input for _ in range(N)]
def s_row_str(N): return [s_list() for _ in range(N)]
def s_row_list(N): return [list(s_input()) for _ in range(N)]


def main():
    import bisect
    N,M = i_map()
    A = i_list()
    BC = [i_list() for i in range(M)]

    BC.sort(key=lambda x: x[1], reverse=True)

    temp = []
    for i in range(M):
        temp += [BC[i][1]] * BC[i][0]
        if len(temp) > N:
            break
    
    A += temp
    A.sort(reverse=True)
    print(sum(A[:N]))
  


  
def __starting_point():
    main()
__starting_point()