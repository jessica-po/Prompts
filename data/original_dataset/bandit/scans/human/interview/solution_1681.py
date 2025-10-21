n = input().rstrip()
m = input().rstrip()
cnt1 = [0] * 26
cnt2 = [0] * 26
for i in n:
    cnt1[ord(i) - ord("a")] += 1
for i in m:
    cnt2[ord(i) - ord("a")] += 1
res = 0
for i in range(26):
    a1 = cnt1[i]
    a2 = cnt2[i]
    if a1 == 0 and a2 != 0:
        print(-1)
        return
    res += min(a1, a2)
print(res)