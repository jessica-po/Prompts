import sys
input = sys.stdin.readline
n=int(input())
a=list(map(int,input().split()))
planks=[0]*100000
pairs=0
squares=0
for x in a:
    planks[x-1]+=1
    if planks[x-1]%2==0:
        pairs+=1
        if planks[x-1]%4==0:
            squares+=1
for f in range(int(input())):
    inp=list(input().split())
    p=inp[0]
    i=int(inp[1])
    i-=1
    if p=="+":
        planks[i]+=1
        if planks[i]%2==0:
            pairs+=1
            if planks[i]%4==0:
                squares+=1
    else:
        if planks[i]%2==0:
            pairs-=1
            if planks[i]%4==0:
                squares-=1
        planks[i]-=1
    if squares>0 and pairs>3:
        print("YES")
    else:
        print("NO")