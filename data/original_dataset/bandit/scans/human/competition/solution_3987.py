n = int(input())
*A, = list(map(int, input().split()))

seq = []
cur = 1; cnt = 0
for a in A:
    if cur == a:
        cnt += 1
    else:
        seq.append(cnt)
        cur = a; cnt = 1
if cnt > 0:
    seq.append(cnt)
ans = max(seq)

l = len(seq)
dp = [[0]*4 for i in range(l+1)]
for i in range(l):
    one = i % 2 #12
    s = seq[i]
    for j in range(4):
        dp[i+1][j] = max(dp[i+1][j], dp[i][j])
        if not one: # 2
            if j % 2 == 0:
                dp[i+1][j] = max(dp[i+1][j], dp[i][j] + s)
            else:
                if j == 1:
                    dp[i+1][j+1] = max(dp[i+1][j+1], dp[i][j] + s)
        else: # 1
            if j % 2 == 1:
                dp[i+1][j] = max(dp[i+1][j], dp[i][j] + s)
            else:
                dp[i+1][j+1] = max(dp[i+1][j+1], dp[i][j] + s)
#    print(dp[i+1])
print(max(dp[l]))