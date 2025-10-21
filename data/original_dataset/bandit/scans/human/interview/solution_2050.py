'''
Created on Oct 12, 2014

@author: Ismael
'''
#import time

from fractions import gcd

def checkSet(setK,newVal):
    for v in setK:
        if(gcd(v,newVal) != 1):
            return False
    return True

def solve(n,k):
    j = 1
    sets = []
    for _ in range(n):
        setK = set()
        while(len(setK) < 4):
            if(checkSet(setK,j) and not(len(setK) == 0 and j%3==0)):
                setK.add(j)
            j += 1
        sets.append(setK)
    maxV = 0
    for setK in sets:
        maxV = max(maxV,max(setK))
    print(maxV*k)
    for setK in sets:
        print(' '.join([str(x*k) for x in setK]))
    
#t = time.clock()
n,k = list(map(int,input().split()))
solve(n,k)
#print(time.clock()-t)