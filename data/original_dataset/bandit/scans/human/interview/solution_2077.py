from sys import stdin, stdout
import os,sys,__pypy__

def main():
    #t = int(stdin.readline())
    n,m = list(map(int, stdin.readline().split()))
    tree = [list() for _ in range(n+1)]
    mn = [0] * (n+1)
    for _ in range(m):
        a,b = list(map(int, stdin.readline().split()))
        tree[a].append(b)
        tree[b].append(a)
    stacks = [list() for _ in range(n+1)]
    arr = list(map(int, stdin.readline().split()))
    for i,x in enumerate(arr):
        stacks[x].append(i+1)
        
    is_can = True
    ans = __pypy__.builders.StringBuilder()
    cnt = 0
    for i,stack in enumerate(stacks):
        for x in stack:
            if mn[x] + 1 == i:
                ans.append("%d "%(x))
                cnt += 1
                for near in tree[x]:
                    if mn[near] +1 == i:
                        mn[near] += 1
            else:
                is_can = False
                break
        if not is_can:
            break
    if not is_can  or cnt != n:
        stdout.write("-1\n")
    else:
        os.write(1,ans.build().encode())
        
main()