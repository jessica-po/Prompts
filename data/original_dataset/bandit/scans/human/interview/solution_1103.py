import copy

def solve():
    n = int(input())
    a = [int(c)-1 for c in input().split(' ')]

    nextcard = [[-1 for i in range(8)] for j in range(n)]
    for i in range(n-2, -1, -1):
        nextcard[i] = copy.copy(nextcard[i+1])
        nextcard[i][a[i+1]] = i+1

    jump = [[-1 for i in range(n+1)] for j in range(n)]
    for i in range(n):
        card = a[i]
        cpos = i
        j = 1
        
        while cpos != -1:
            jump[i][j] = cpos
            j+=1
            cpos = nextcard[cpos][card]

    #Find dp solution for range (val, val+1)
    def getLen(val):
        dp = [[-1 for i in range(1<<8)] for j in range(n+1)]
        dp[0][0] = 0

        for i in range(n):
            card = a[i]
            for comb in range(1<<8):
                if (comb & (1<<card)) == 0 and dp[i][comb] != -1:
                    ncomb = comb + (1<<card)
                    
                    if jump[i][val] != -1:
                        j = jump[i][val]+1
                        dp[j][ncomb] = max(dp[j][ncomb], dp[i][comb] + val)
                        
                    if jump[i][val+1] != -1:
                        j = jump[i][val+1]+1
                        dp[j][ncomb] = max(dp[j][ncomb], dp[i][comb] + val + 1)

                dp[i+1][comb] = max(dp[i+1][comb], dp[i][comb])

        return dp[n][(1<<8)-1]

    appear = [False for i in range(8)]
    for c in a:
        appear[c] = True

    result = 0
    for c in appear:
        result += int(c)

    #Finally binary search to find the result

    cur = 0
    for lev in range(9, -1, -1):
        tpow = (1<<lev)
        if cur + tpow < n:
            ret = getLen(cur + tpow)

            if(ret != -1):
                result = max(result, ret)
                cur += tpow

    return result

print(solve())