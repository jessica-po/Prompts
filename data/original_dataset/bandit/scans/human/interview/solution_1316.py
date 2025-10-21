n, k = [int(i) for i in input().split()]

dic = dict()

s = list(input())

i = 0
while i<n:
    j = 1
    while i+j < n and s[i] == s[i+j]:
        j+=1
    if s[i] not in dic:
        dic[s[i]] = []
    dic[s[i]].append(j)
    i += j
ans = 0

for i in list(dic.keys()):
    ct = 0
    for j in dic[i]:
        ct+=(j//k)
    ans = max(ans, ct)
    #if min(dic[i]) >= k:
        #ans = max(ans, min(dic[i]))

print(ans)