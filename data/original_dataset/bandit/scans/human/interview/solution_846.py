n, m = map(int,input().split())
b = list(map(int,input().split()))
ans = [-1]*101
for bb in b:
    for i in range(bb,n+1):
        if ans[i]==-1:
            ans[i]=bb
print(*ans[1:n+1])