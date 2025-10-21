import sys
input = sys.stdin.readline
for f in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    a.sort()
    mx=1
    for i in range(n):
        if a[i]<=i+1:
            mx=i+2
    print(mx)