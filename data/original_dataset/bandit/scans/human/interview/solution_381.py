import math,string,itertools,fractions,heapq,collections,re,array,bisect
from itertools import chain, dropwhile, permutations, combinations
from collections import defaultdict, deque

def VI(): return list(map(int,input().split()))

def main1(k):
    # works correctly, but too slow and generates many more vertices than necessary.
    # doesn't pass the time constraint with this implementation. (prints 10^5 lines)
    # ==> use the editorial solution below.
    if k%2==0:
        print("NO")
        return
    print("YES")
    n = 2*(k**2-k+1)
    m = n*k//2
    print(n, m)
    i = 0
    g = [[] for i in range(n+1)]
    print(1,n//2+1)
    off = 1
    for j in range(0,k-1,2):
        j1 = off + j+1
        j2 = off + j+2
        print(off,j1)
        print(off,j2)
        l1 = off + k + j*(k-1)
        l2 = off + k + (j+1)*(k-1)
        for l in range(k-1):
            print(j1, l1+l)
            print(j2, l2+l)
            for m in range(k-1):
                print(l1+l,l2+m)
    off = n//2+1
    for j in range(0,k-1,2):
        j1 = off + j+1
        j2 = off + j+2
        print(off,j1)
        print(off,j2)
        l1 = off + k + j*(k-1)
        l2 = off + k + (j+1)*(k-1)
        for l in range(k-1):
            print(j1, l1+l)
            print(j2, l2+l)
            for m in range(k-1):
                print(l1+l,l2+m)

def main(k):
    # following the editorial algo
    if k%2==0:
        print("NO")
        return
    print("YES")
    if k==1:
        print("2 1")
        print("1 2")
        return
    n = 2*k+4
    m = n*k//2
    e = []
    e.extend([(1,n//2+1)])
    off = 1
    for j in range(off+1,off+k):
        e.extend([(off, j)])
    for j in range(off+1,off+k):
        for i in range(j+1,off+k):
            if (i==j+1 and (j-off)%2==1):# or (j==off+1 and i==off+k-1):
            #if (i==j+1 and i%2==0) or (j==off+1 and i==off+k-1):
                continue
            e.extend([(j,i)])
        e.extend([(j,off+k),(j,off+k+1)])
    e.extend([(off+k,off+k+1)])
    off = n//2+1
    for j in range(off+1,off+k):
        e.extend([(off, j)])
    for j in range(off+1,off+k):
        for i in range(j+1,off+k):
            if (i==j+1 and (j-off)%2==1):# or (j==off+1 and i==off+k-1):
                continue
            e.extend([(j,i)])
        e.extend([(j,off+k),(j,off+k+1)])
    e.extend([(off+k,off+k+1)])
    print(n, m)
    for x in e:
        print(*x)



def main_input(info=0):
    k = int(input())
    main(k)

def __starting_point():
    main_input()

__starting_point()