n = int(input())
mod = 10**9+7
a = []
l = ["A","C","G","T"]
ban = ["AAGC","CAGC","GAGC","TAGC","AGCA","AGCC","AGCG","AGCT","AGAC","CGAC","GGAC","TGAC","GACA","GACC","GACG","GACT","AACG","CACG","GACG","TACG","ACGA","ACGC","ACGG","ACGT","ATGC","ACGC","AGGC","AGTC","AGGC","AGAC"]
for i in l:
    for j in l:
        for k in l:
            a.append(i+j+k)
dp = [[0]*64 for _ in range(n+1)]
for i in range(64):
    if (a[i]=="AGC" or a[i]=="ACG" or a[i]=="GAC"):
        continue
    dp[3][i] = 1
for i in range(4,n+1):
    for j in range(64):
        for k in l:
            b = a[j]+k
            if b in ban:
                continue
            else:
                dp[i][a.index(b[1:])] += dp[i-1][j]
                dp[i][a.index(b[1:])] %= mod
print((sum(dp[-1])%mod))