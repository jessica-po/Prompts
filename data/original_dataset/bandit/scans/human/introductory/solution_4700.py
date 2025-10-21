N,M = map(int,input().split())
high = list(map(int,input().split()))
ans = [0]*N
cnt = 0
for i in range(M):
    a,b = map(int,input().split())
    ans[a-1] = max(high[b-1],ans[a-1])
    ans[b-1] = max(ans[b-1],high[a-1])

for j in range(N):
    if ans[j] < high[j]:
        cnt += 1
print(cnt)