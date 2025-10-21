q=int(input())
for t in range(q):
    a,b,n,s=map(int,input().split())
    v=min(a*n,s//n*n)
    if s-v>b:
        print("NO")
    else:
        print("YES")