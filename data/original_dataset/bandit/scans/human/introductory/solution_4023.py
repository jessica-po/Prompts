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
za = getIntList()

mh = max(za)
za.append(mh)

duo = [(mh,0)]

for i in range(N+1):
    h = za[i]
    while duo:
        if i%2 != duo[-1][1]%2:
            dprint(i )
            print('NO')
            return
        if h >= duo[-1][0]:
            lh = duo[-1][0]
            duo.pop()
            if h== lh:
                break
        else:
            break
    duo.append( (h,i+1))
    #dprint(duo)
print('YES')