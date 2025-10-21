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
s = input()
t = input()

zs = list(s)
zt = list(t)
zs.sort()
zt.sort()
if zs != zt:
    print(-1)
    return

zs = list(s)

res = []
for i in range(N):
    if zs[i] == t[i]: continue
    for j in range(i+1,N):
        if zs[j] == t[i]: break
    for k in range(j-1,i-1, -1):
        res.append(k)
        zs[k],zs[k+1] = zs[k+1],zs[k]

print(len(res))
for x in res:
    print(x+1,end = ' ')