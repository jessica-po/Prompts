import sys



n = int(sys.stdin.readline().strip())
s = sys.stdin.readline().strip()

dp = [[-1] * (n + 1) for i in range(26)]


for c in range(26):
    for j in range(n):
        tst = 1 if s[j] == chr(c + 97) else 0
        dp[c][1 - tst] = max(dp[c][1 - tst], 1)
        for k in range(j + 1, n):
            if s[k] == chr(c + 97):tst += 1
            dp[c][k - j + 1 - tst] = max(dp[c][k - j + 1 - tst], k - j + 1)

#for c in range(26):
#    for j in range(n):
#        dp[c][j + 1] = max(dp[c][j], dp[c][j + 1])

q = int(sys.stdin.readline().strip())

for i in range(q):
    m, c = [item for item in sys.stdin.readline().strip().split()]
    m = int(m)
    #print(max([dp[ord(c) - 97][u] for u in range(m + 1)]))
    print(dp[ord(c) - 97][m]) if dp[ord(c) - 97][m] != -1 else print(n)