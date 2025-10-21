#      
import collections, atexit, math, sys, bisect 

sys.setrecursionlimit(1000000)
def getIntList():
    return list(map(int, input().split()))    

try :
    #raise ModuleNotFoundError
    import numpy
    def dprint(*args, **kwargs):
        print(*args, **kwargs, file=sys.stderr)
    dprint('debug mode')
except ModuleNotFoundError:
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
    
N, = getIntList()

zb = []
 
total = 0

de = [0,0,0,0,0]
gr = [ [] for i in range(5)]
minv = 10000000
for i in range(N):
    a,b,c = getIntList()
    de[a]+=1
    de[c] +=1
    zb.append( (a,b,c) )
    total +=b
    if a!=c:
        minv = min(minv,b)
vis = [0,0,0,0,0]

def dfs( root):
    if vis[root]:return []
    vis[root] = 1
    r = [root,]
    for x in zb:
        a,b,c =  x
        if a==root:
            r = r+ dfs(c)
        elif c==root:
            r = r+ dfs(a)
    return r

res = 0
for i in range(1,5):
    if vis[i]:continue
    t = dfs(i)
    t = set(t)
    if len(t) ==4:
        for j in range(1,5):
            if de[j]%2==0:
                print(total)
                return
        print(total-minv)
        return
    tr = 0
    for x in zb:
        a,b,c = x
        if a in t:
            tr +=b
    res = max(res,tr)

print(res)