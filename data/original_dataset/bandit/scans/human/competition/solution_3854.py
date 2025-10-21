#coding gbk
#!usr/bin/ENV
cin =lambda : list(map(int,input().split()))
n, k = cin()
c=list(cin())
dp = [0]*(k+1)
dp[0]=1
for i in c:
    tmp = dp[:]
    for x in range(k,i-1,-1):
        tmp[x] |= dp[x-i]|(dp[x-i]<<i)
    dp = tmp
b = bin(dp[-1])
ans = [i for i in range(k + 1) if b[-i - 1] == '1']
print(len(ans))
print(*ans)