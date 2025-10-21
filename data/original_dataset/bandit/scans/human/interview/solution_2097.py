import sys
import math
import heapq
import bisect
import re
from collections import deque
from decimal import *
from fractions import gcd
 
def YES_NO(flag):
    if flag:
        print("AWW")
    else:
        print("WAW")
 
 
def main():
    # q = [int(i) for i in sys.stdin.readline().split()]
    n = int(sys.stdin.readline())
    q = [int(i) for i in sys.stdin.readline().split()]
    w = q.count(0)
    if w + sum(q) == 0:
        print(w + 1)
    else:
        print(w)
for i in range(int(sys.stdin.readline())):
    main()