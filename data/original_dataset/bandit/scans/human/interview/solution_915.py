k = int(input())
codeforces = "codeforces"
ans = [1 for _ in range(len(codeforces))]
i = 0
tot = 1
while tot < k:
    tot //= ans[i]
    ans[i] += 1
    tot *= ans[i]
    i += 1
    i %= len(codeforces)
for i in range(len(codeforces)):
    print(codeforces[i] * ans[i], end = "")
print()