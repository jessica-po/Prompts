import sys
from sys import stdout
import random
from fractions import Fraction
from math import *
 
def input():
    return sys.stdin.readline().strip()
 
def iinput():
    return int(input())

def finput():
    return float(input())

def tinput():
    return input().split()

def linput():
    return list(input())
 
def rinput():
    return list(map(int, tinput()))

def fiinput():
    return list(map(float, tinput()))
 
def rlinput():
    return list(map(int, input().split()))
def trinput():
    return tuple(rinput())

def srlinput():
    return sorted(list(map(int, input().split())))

def NOYES(fl):
    if fl:
        print("NO")
    else:
        print("YES")
def YESNO(fl):
    if fl:
        print("YES")
    else:
        print("NO")
    
def main():
    def answer(res):
        print((res + 1) // 2)
    n = iinput()
    #k = iinput() 
    #m = iinput() 
    #n = int(sys.stdin.readline().strip()) 
    #n, k = rinput()
    #n, m = rinput()
    #m, k = rinput()
    #n, k, m = rinput()
    #n, m, k = rinput()
    #k, n, m = rinput()
    #k, m, n = rinput() 
    #m, k, n = rinput()
    #m, n, k = rinput()
    #q = srlinput()
    #q = linput()
    q = rlinput()
    w = [0] + [q[i] - q[i - 1] for i in range(1, n)]
    res = q[0] + sum([max(w[i], 0) for i in range(1, n)])
    answer(res)
    k = iinput()
    for o in range(k):
        l, r, x = rinput()
        if l == 1:
            res += x        
        else:
            res = res - max(0, w[l - 1]) + max(0, w[l - 1] + x); w[l - 1] += x 
        if r != n:
            res = res - max(0, w[r]) + max(0, w[r] - x); w[r] -= x 
        answer(res)
    
        
    
    
        
    

for i in range(1):
    main()