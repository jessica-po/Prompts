#credits https://www.geeksforgeeks.org/minimum-steps-to-delete-a-ssing-after-repeated-deletion-of-palindrome-subssings/
  
n=int(input())
s=input()
N = len(s)
dp = [[0 for x in range(N + 1)] 
         for y in range(N + 1)]
D = [[[] for x in range(N + 1)] 
         for y in range(N + 1)]
ss=""
re=""
for i in range(0,N):
    if re!=s[i]:
        ss+=re
        re=s[i]
ss+=re
a=ss
N=len(a)
for l in range(1, N + 1): 
    i = 0
    j = l - 1
    while j < N: 
        if (l == 1): 
            dp[i][j] = 1
        else: 

            dp[i][j] =1+dp[i + 1][j]

            for K in range(i + 1, j + 1): 
                if (a[i] == a[K]):
                        if dp[i][j]>=dp[i ][K - 1] + dp[K + 1][j]:
                            dp[i][j] = dp[i][K - 1] + dp[K + 1][j]

                        
                      
        i += 1
        j += 1

print(dp[0][N-1])