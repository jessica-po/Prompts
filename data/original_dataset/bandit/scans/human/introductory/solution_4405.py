#      
import collections, atexit, math, sys, bisect 

sys.setrecursionlimit(1000000)
def getIntList():
    return list(map(int, input().split()))    

try :
    #raise ModuleNotFoundError
    import numpy
    def dprint(*args, **kwargs):
        #print(*args, **kwargs, file=sys.stderr)
        # in python 3.4 **kwargs is invalid???
        print(*args,  file=sys.stderr)
    dprint('debug mode')
except Exception:
    def dprint(*args, **kwargs):
        pass



inId = 0
outId = 0
if inId>0:
    dprint('use input', inId)
    sys.stdin = open('input'+ str(inId) + '.txt', 'r') #标准输出重定向至文件
if outId>0:
    dprint('use output', outId)
    sys.stdout = open('stdout'+ str(outId) + '.txt', 'w') #标准输出重定向至文件
    atexit.register(lambda :sys.stdout.close())     #idle 中不会执行 atexit
    
N  = getIntList()
za  = getIntList()

cc = collections.Counter(za)
zt = []
for x in cc:
    zt.append( cc[x] )

zt.sort( )

re = zt[-1] 

def findmid(l,r, e):
    if l>= len(zt):
        return -1
    if e<=zt[l]: return l;
    if e>zt[r]: return -1
    while l+1 <r:
        mid = (l+r)//2
        if zt[mid] < e:
            l = mid
        else:
            r = mid
    return r
for first in range(1, re//2 + 1):
    nowr = 0
    t = first
    ind = -1
    while 1:
        ind = findmid(ind+1,len(zt)-1, t)
        if ind<0:
            break
        nowr += t
        t*=2
    re = max(re, nowr)
print(re)