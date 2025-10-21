# coding: utf-8
# Your code here!
import sys
readline = sys.stdin.readline
read = sys.stdin.read

n, = map(int,input().split())
*a, = map(int,input().split())

if all(i <= 0 for i in a):
    m = max(a)
    idx = a.index(m)
    print(m)
    print(n-1)
    for i in range(idx):
        print(1)
    for i in range(n-idx-1):
        print(n-idx-i)
    return

even = a[::2]
odd = a[1::2]

se = sum(i for i in even if i > 0)
so = sum(i for i in odd  if i > 0)

res = []
if se < so:
    res.append(1)
    a.pop(0)
    n -= 1
# 0,2,4,6,....-th から
if len(a)%2==0:
    res.append(n)
    a.pop()
    n -= 1
while len(a) > 1:
    n = len(a)
    if a[-1] <= 0:
        res.append(n)
        a.pop()
        res.append(n-1)
        a.pop()
    else:
        if a[-3] > 0:
            res.append(n-1)
            a[-3] += a[-1]
            a.pop()
            a.pop()
        else:
            if len(a) == 3:
                res += [1,1]
                a.pop(0)
                a.pop(0)
            else:
                res.append(n-2)
                a.pop(n-3)
                a.pop(n-3)


assert a[0] == max(se,so)
print(max(se,so))
print(len(res))
print(*res,sep="\n")