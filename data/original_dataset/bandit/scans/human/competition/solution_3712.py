#! /usr/bin/env python

n = int(input())
counts = [0] * 5
nums = [int(x) for x in input().split()]
for x in nums:
    counts[x] += 1

s = sum(nums)
if s > 2 and s != 5:
    ans = 0
    if counts[1] >= counts[2]:
        ans += counts[2]
        counts[3] += counts[2]
        counts[1] -= counts[2]
        ans += 2 * (counts[1] // 3)
        counts[3] += counts[1] // 3
        counts[1] %= 3
        if counts[3] > 0:
            ans += counts[1]
        elif counts[1] != 0:
            ans += 2
    else:
        ans += counts[1]
        counts[2] -= counts[1]
        ans += 2 * (counts[2] // 3)
        counts[2] %= 3
        if counts[4] > 0:
            ans += counts[2]
        elif counts[2] != 0:
            ans += 2
    print(ans)
else:
    print(-1)