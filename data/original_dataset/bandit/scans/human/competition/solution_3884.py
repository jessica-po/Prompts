#      
import collections, atexit, math, sys
from functools import cmp_to_key
#key=cmp_to_key(lambda x,y: 1 if x not in y else -1 )

sys.setrecursionlimit(1000000)
def getIntList():
    return list(map(int, input().split()))    

import bisect 
try :
    #raise ModuleNotFoundError
    import numpy
    def dprint(*args, **kwargs):
        print(*args, **kwargs, file=sys.stderr)
    dprint('debug mode')
except ModuleNotFoundError:
    def dprint(*args, **kwargs):
        pass


def memo(func):  
    cache={}  
    def wrap(*args):  
        if args not in cache:  
            cache[args]=func(*args)  
        return cache[args]  
    return wrap

@memo
def comb (n,k):
    if k==0: return 1
    if n==k: return 1
    return comb(n-1,k-1) + comb(n-1,k)

inId = 0
outId = 0
if inId>0:
    dprint('use input', inId)
    sys.stdin = open('input'+ str(inId) + '.txt', 'r') #标准输出重定向至文件
if outId>0:
    dprint('use output', outId)
    sys.stdout = open('stdout'+ str(outId) + '.txt', 'w') #标准输出重定向至文件
    atexit.register(lambda :sys.stdout.close())     #idle 中不会执行 atexit
    
N, = getIntList()
M, = getIntList()
za = getIntList()
zb = getIntList()

if 1 in za or 1 in zb:
    print(-1)
    return
    

def trywork(fuel):
    for i in range(N):
        now = fuel + M
        cost = now / za[i]
        fuel-=cost
        if fuel <0: return False
        now = fuel +M
        cost = now / zb[ (i+1)%N]
        fuel-=cost
        if fuel<0: return False
    return True

r0 = 0
r1 = 10**9+1


while r1-r0 > 1e-7 and (r1-r0) *10000000 >r1:
    m = (r1+r0)/2
    f = trywork(m)
    if f:
        r1 = m
    else:
        r0 = m

print(r1)