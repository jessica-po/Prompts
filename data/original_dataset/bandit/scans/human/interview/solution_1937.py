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
    
N, = getIntList()
#print(N)

zb = getIntList()

za1 = [0]
za2 = [zb[0]]

for i in range(1, N//2):
    t1 = zb[i] - za1[-1]
    if t1 <= za2[-1]:
        za1.append(za1[-1])
        za2.append(t1)
        continue
    t2 = zb[i] - za2[-1]
    if t2 >= za1[-1]:
        za1.append(t2)
        za2.append(za2[-1])
        continue
    assert False

zr = za1 + za2[ : :-1]
zs = []
for x in zr:
    zs .append(str(x))
    

r = ' '.join(zs)

print(r)