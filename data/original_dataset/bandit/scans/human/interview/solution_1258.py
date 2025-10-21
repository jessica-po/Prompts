from bisect import *
from collections import *
from itertools import *
import functools
import sys
import math
from decimal import *
from copy import *
from heapq import *
from fractions import *
getcontext().prec = 30
MAX = sys.maxsize
MAXN = 1000010
MOD = 10**9+7
spf = [i for i in range(MAXN)]
def sieve():
    for i in range(2,MAXN,2):
        spf[i] = 2
    for i in range(3,int(MAXN**0.5)+1):
        if spf[i]==i:
            for j in range(i*i,MAXN,i):
                if spf[j]==j:
                    spf[j]=i
def fib(n,m):
    if n == 0:
        return [0, 1]
    else:
        a, b = fib(n // 2)
        c = ((a%m) * ((b%m) * 2 - (a%m)))%m
        d = ((a%m) * (a%m))%m + ((b)%m * (b)%m)%m
        if n % 2 == 0:
            return [c, d]
        else:
            return [d, c + d]

def charIN(x= ' '):
    return(sys.stdin.readline().strip().split(x))

def arrIN(x = ' '):
    return list(map(int,sys.stdin.readline().strip().split(x)))

def ncr(n,r):
    num=den=1
    for i in range(r):
        num = (num*(n-i))%MOD
        den = (den*(i+1))%MOD

    return (num*(pow(den,MOD-2,MOD)))%MOD

def flush():
    return sys.stdout.flush()

'''*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*'''
n = int(input())
a = [arrIN() for _ in range(n-2)]
d = [0]*(n+1)
pos = defaultdict(list)
for i in range(n-2):
    for j in a[i]:
        d[j]+=1
        pos[j].append(i)
ans = []
flag = [1]*(n-2)
for i in range(1,n+1):
    if d[i]==1:
        x  = a[pos[i][0]]
        flag[pos[i][0]] = 0
        break
t = [0,0,0]
for i in x:
    if d[i]==1:
        t[0] = i
    elif d[i]==2: 
        t[1] = i
    else:
        t[2] = i
ans = t
l = 3
while l!=n:
    for i in pos[ans[-2]]:
        if flag[i]:
            if ans[-1] in a[i]:
                x = a[i]
                flag[i] = 0
                break

    t = [i for i in x]
    t.remove(ans[-2])
    t.remove(ans[-1])
    ans.append(t[0])
    l+=1
print(*ans)