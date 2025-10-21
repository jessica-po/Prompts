import sys
import math


def main():
    n,t,k = map(int,sys.stdin.readline().split())
    a = list(map(int,sys.stdin.readline().split()))

    g = [[] for i in range(t+1)]
    g[0].append([1,-1,0])
    c = 1
    for i in range(t):
        for j in range(a[i]):
            c+=1
            g[i+1].append([c,0,0])
            g[i][0][2]+=1

    l=0
    for i in range(1,t+1):
        for j in range(len(g[i])):
            if g[i][j][2]==0:
                l+=1
    if l< k:
        print(-1)
        return

    i=0
    j=0
    m = 1
    while l>k and m<t:
        while i< len(g[m]) and g[m][i][2]>0:
            i+=1
        if i>=len(g[m]):
            i=0
            j=0
            m+=1
            continue
        while j<len(g[m+1]) and g[m][g[m+1][j][1]][2]<2:
            j+=1
        if j>=len(g[m+1]):
            i=0
            j=0
            m+=1
            continue
        g[m][i][2]+=1
        g[m][g[m+1][j][1]][2]-=1
        g[m+1][j][1] = i
        l-=1
        i+=1
        j+=1

    if l!=k:        
        print(-1)
        return
    print(n)
    for i in range(1,t+1):
        for j in range(len(g[i])):
            print(g[i][j][0], g[i-1][g[i][j][1]][0])


main()