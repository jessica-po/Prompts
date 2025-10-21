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
    
N, M= getIntList()

ne = [0 for i in range(N+1) ]
za = getIntList()
for i in range(N-1):
    ne[ za[i]] = za[i+1]
ne[za[-1]] = 0

for _ in range(1, M):
    za = getIntList()
    for i in range(N-1):
        a = za[i]
        b = za[i+1]
        if ne[a] != b:
            ne[a] = -1
    a = za[-1]
    if ne[a]!=0:
        ne[a] = -1

tin = [0 for i in range(N+1) ]

for i in range(1,N+1):
    a = ne[i]
    if a>0:
        tin[a] = 1

res = 0
for i in range(1,N+1):
    if tin[i]: continue
    n = 0
    while i>0:
        n+=1
        i = ne[i]
    res += n * (n+1) //2

print(res)