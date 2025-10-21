#      
import collections, atexit, math, sys, bisect 

sys.setrecursionlimit(1000000)

isdebug = False
try :
    #raise ModuleNotFoundError
    import pylint
    import numpy
    def dprint(*args, **kwargs):
        #print(*args, **kwargs, file=sys.stderr)
        # in python 3.4 **kwargs is invalid???
        print(*args,  file=sys.stderr)
    dprint('debug mode')
    isdebug = True
except Exception:
    def dprint(*args, **kwargs):
        pass


def red_inout():
    inId = 0
    outId = 0
    if not isdebug:
        inId = 0
        outId = 0
    if inId>0:
        dprint('use input', inId)
        try:
            f = open('input'+ str(inId) + '.txt', 'r')
            sys.stdin = f #标准输出重定向至文件
        except Exception:
            dprint('invalid input file')
    if outId>0:
        dprint('use output', outId)
        try:
            f = open('stdout'+ str(outId) + '.txt', 'w')
            sys.stdout = f #标准输出重定向至文件
        except Exception:
            dprint('invalid output file')
            
        atexit.register(lambda :sys.stdout.close())     #idle 中不会执行 atexit

if isdebug and len(sys.argv) == 1:
    red_inout()

def getIntList():
    return list(map(int, input().split()))            

def solve(): 
    pass
    
T_ = 1    
T_, = getIntList()

for iii_ in range(T_):
    #solve()
    N,  = getIntList()
    #print(N)
    s = input()
    r = 0
    for i in range(N):
        if s[i] =='>':
            r = i
            break
    r1 = 0
    for i in range(N-1, -1, -1):
        if s[i]=='<':
            r1 = N-1-i
            break
    print(min(r,r1))