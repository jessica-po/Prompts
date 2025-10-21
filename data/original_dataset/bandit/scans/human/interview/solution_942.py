input()
l = list(map(int, input().split()))
d = {}
d2 = {}
ans = []
n = 1
for i in l:
    i = len(l) - i
    if i not in d:
        d[i] = n
        n += 1
    if i not in d2:
        d2[i] = 0
    if d2[i] >= i:
        d[i] = n
        d2[i] = 0
        n += 1
    ans.append(d[i])
    d2[i] += 1
nums = {}
tot = 0
for i in ans:
    tot += 1
    if i not in nums:
        nums[i] = 0
    nums[i] += 1
for i in range(len(ans)):
    if tot - nums[ans[i]] != l[i]:
        print("Impossible")
        return
print("Possible")
print(" ".join(map(str, ans)))