import sys
input = sys.stdin.readline

N, K = list(map(int, input().split()))
nums = []
for i in range(N):
    t, d = list(map(int, input().split()))
    nums.append((d, t))
nums.sort(reverse=True)
se = set()
a1 = []
a2 = []
rest = []
for i, n in enumerate(nums):
    if i < K:
        if not n[1] in se:
            se.add(n[1])
            a1.append(n)
        else:
            a2.append(n)
    else:
        rest.append(n)
points = 0
for (d, t) in a1: points += d
for (d, t) in a2: points += d
ans = points + pow(len(se), 2)
a2.sort()
idx2 = 0
for i, (d, t) in enumerate(rest):
    if t in se: continue
    if len(a2) <= idx2: break
    points -= a2[idx2][0]
    idx2 += 1
    points += d
    se.add(t)
    ans = max(ans, points+pow(len(se), 2))
print(ans)