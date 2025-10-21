#!/usr/bin/pypy3

from sys import stdin,stderr
import random
import cProfile

def readInts(): return map(int,stdin.readline().strip().split())
def print_err(*args,**kwargs): print(*args,file=stderr,**kwargs)
    
def solve(vs):
    return None

def generate_tree(n,ns):
    out = [0 for _ in range(2**(n+1))]
    def gt(nix,left,right,op):
        if left+1==right:
            out[nix] = ns[left]
            return out[nix]
        mid = (left+right)//2
        nL = nix*2+1
        nR = nix*2+2
        vL = gt(nL,left,mid,not op)
        vR = gt(nR,mid,right,not op)
        if op: v = vL ^ vR
        else: v = vL | vR
        out[nix] = v
        return v
    gt(0,0,2**n,n%2==0)
    return out

def alter_tree2(n,t,p,b):
    def at(nix,width,offp,op):
        if width==1:
            t[nix]=b
            return b
        width //= 2
        nL = nix*2+1
        nR = nix*2+2
        vL = t[nL]
        vR = t[nR]
        if offp >= width: vR = at(nR,width,offp-width,not op)
        else: vL = at(nL,width,offp,not op)
        if op: v = vL ^ vR
        else: v = vL | vR
        t[nix] = v
        return v
    at(0,2**n,p,n%2==0)
            
def alter_tree(n,t,p,b):
    width = 2**n
    s = []
    nix = 0
    op = (n%2==0)
    while width>1:
        width //= 2
        #print(nix)
        if p >= width:
            nix2 = 2*nix+2
            s.append( (nix,nix2-1) )
            p -= width
        else:
            nix2 = 2*nix+1
            s.append( (nix,nix2+1) )
        nix = nix2
        op = not op
    #print(nix)
    t[nix] = b
    v = b
    while s:
        nix,nixO = s.pop()
        if op: v |= t[nixO]
        else: v ^= t[nixO]
        t[nix] = v        
        op = not op
    return
    
def run():
    n,m = readInts()    
    axs = list(readInts())
    t = generate_tree(n,axs)
    for _ in range(m):
        p,b = readInts()
        alter_tree(n,t,p-1,b)
        print(t[0])

def test():
    n = 17
    ns = []
    vs100 = list(range(100))
    for _ in range(2**17):
        ns.append(random.choice(vs100))        
    t = generate_tree(n,ns)
    t2 = generate_tree(n,ns)
    for _ in range(100000):
        v1 = random.choice(vs100)
        v2 = random.choice(vs100)
        alter_tree(n,t,v1,v2)
        alter_tree2(n,t2,v1,v2)
    print(all(map(lambda x: x[0]==x[1],zip(t,t2))))
    print(t[0]==t2[0])
    
run()