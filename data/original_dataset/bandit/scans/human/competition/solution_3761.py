from sys import setrecursionlimit, stderr
from functools import reduce
from itertools import *
from collections import defaultdict
from bisect import *

def read():
  return int(input())
 
def reads():
  return [int(x) for x in input().split()]

S = input()
x, y = reads()
qs = [len(s) for s in S.split('T')]

def knapsack(xs, target):
  es = {0}
  for x in xs:
    es = {e - x for e in es} | {e + x for e in es}
  return target in es

ans = knapsack(qs[2::2], x-qs[0]) and knapsack(qs[1::2], y)
print("Yes" if ans else "No")