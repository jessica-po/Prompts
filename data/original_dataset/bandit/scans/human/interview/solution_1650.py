MOD = 10**9 + 7

s = str(input())

dp0 = [0] * (len(s)+1)
dp1 = [0] * (len(s)+1)
dp0[0] = 1

for i in range(1,len(s)+1):
    if s[i-1] == "0":
        dp0[i] = dp0[i-1]
        dp1[i] = dp1[i-1] * 3
    else:
        dp0[i] = dp0[i-1] * 2
        dp1[i] = dp0[i-1] + dp1[i-1] * 3
    dp0[i] %= MOD
    dp1[i] %= MOD

answer = dp0[-1] + dp1[-1]
if answer >= MOD:
    answer -= MOD
print(answer)