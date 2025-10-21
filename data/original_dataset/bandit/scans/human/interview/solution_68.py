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
    
N, = getIntList()
#print(N)
S = input()

X, Y = getIntList()

dd = ( (0,1), (0,-1), (-1,0), (1,0))
pp = 'UDLR'
zz = {}
for i in range(4):
    zz[ pp[i]] = dd[i]


if abs(X) + abs(Y) >N:
    print(-1)
    return

if abs(X+Y-N)%2==1:
    print(-1)
    return
    
fromLeft = [None for i in range(N)]
fromRight = fromLeft.copy()

x0 = 0
y0 = 0
for i in range(N):
    x = S[i]
    fromLeft[i] = (x0,y0)
    g = zz[x]
    x0+= g[0]
    y0+= g[1]

if x0==X and y0==Y:
    print(0)
    return

x0 = 0
y0 = 0
for i in range(N-1,-1,-1):
    x = S[i]
    fromRight[i] = (x0,y0)
    g = zz[x]
    x0+= g[0]
    y0+= g[1]


up = N
down = 0
dprint(fromLeft)
dprint(fromRight)
while down+1<up:
    mid = (up+down)//2
    dprint('mid', mid)
    ok = False
    for i in range(N-mid + 1):
        tx = fromLeft[i][0] + fromRight[i+mid-1][0]
        ty = fromLeft[i][1] + fromRight[i+mid-1][1]
        gg = abs(X-tx) + abs(Y- ty)
        if gg <= mid:
            ok = True
            break
    if ok:
        up = mid
    else:
        down = mid
        
print(up)