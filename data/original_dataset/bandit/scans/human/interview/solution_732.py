#CF Round 150. Div II Prob. A - Dividing Orange
import sys

dp = [[[-1 for j in range(3)] for i in range (1 << 10)] for k in range(11)]

In = sys.stdin
n = In.readline().strip()

def go (idx, mask, equal):
    if dp[idx][mask][equal] != -1:
        return dp[idx][mask][equal]
    if bin(mask).count("1") > 2:
        return 0
    if idx == len(n):
        return 1
    res = 0
    if idx == 0 or equal == 2:
        res += go(idx + 1, mask, 2)
    elif equal == 1 and int(n[idx]) == 0:
        res += go(idx + 1, mask | 1, 1)
    else:
        res += go(idx + 1, mask | 1, 0)    
    for i in range(1, 10):
        if equal == 1 and i > int(n[idx]):
            break
        elif equal == 1 and i == int(n[idx]):
            res += go(idx + 1, mask | (1 << i), 1)
        else:
            res += go(idx + 1, mask | (1 << i), 0)
    dp[idx][mask][equal] = res
    return res
    
print(go(0, 0, 1)  - 1)