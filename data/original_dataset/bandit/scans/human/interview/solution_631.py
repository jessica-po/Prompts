import sys
input=sys.stdin.readline

T=int(input())
for _ in range(T):
    n,m=list(map(int,input().split()))
    A=list(map(int,input().split()))
    s=sum(A)
    if (s==m):
        print("YES")
    else:
        print("NO")