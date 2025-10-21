import sys
# import math
# import bisect
# import numpy as np
# from decimal import Decimal
# from numba import njit, i8, u1, b1 #JIT compiler
# from itertools import combinations, product
# from collections import Counter, deque, defaultdict

# sys.setrecursionlimit(10 ** 6)
MOD = 10 ** 9 + 7
INF = 10 ** 9
PI = 3.14159265358979323846

def read_str():      return sys.stdin.readline().strip()
def read_int():      return int(sys.stdin.readline().strip())
def read_ints():     return map(int, sys.stdin.readline().strip().split())
def read_ints2(x):   return map(lambda num: int(num) - x, sys.stdin.readline().strip().split())
def read_str_list(): return list(sys.stdin.readline().strip().split())
def read_int_list(): return list(map(int, sys.stdin.readline().strip().split()))
def GCD(a: int, b: int) -> int: return b if a%b==0 else GCD(b, a%b)
def LCM(a: int, b: int) -> int: return (a * b) // GCD(a, b)

def solve(info):
    for Cx in range(101):
        for Cy in range(101):
            height = abs(Cx - info[0][0]) + abs(Cy - info[0][1]) + info[0][2]
            flag = True
            for x,y,h in info[1:]:
                val = max(height - abs(Cx - x) - abs(Cy - y), 0)
                if h == val:
                    continue
                else:
                    flag = False
                    break
            if flag:
                return Cx, Cy, height

def Main():
    n = read_int()
    info = [tuple(read_ints()) for _ in range(n)]
    info.sort(key=lambda x: x[2], reverse=True)

    print(*solve(info))

def __starting_point():
    Main()
__starting_point()