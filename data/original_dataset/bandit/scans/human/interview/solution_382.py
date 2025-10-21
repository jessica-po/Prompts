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
    
N, M, Q = getIntList()

s1 = input()
s2 = input()

tot = 0
zt = [0]

for i in range(N):
    if s1[i:i+M] == s2:
        tot+=1
    zt.append(tot)
dprint(zt)
for i in range(Q):
    a,b = getIntList()
    b0 = b- M+1
    if b0<a:
        print(0)
    else:
        print(zt[b0] - zt[a-1])