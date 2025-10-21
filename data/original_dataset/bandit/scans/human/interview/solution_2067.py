# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 11/20/18

"""
import collections
import bisect

N, M = map(int, input().split())
vlines = []
for i in range(N):
    x = int(input())
    vlines.append(x)

vlines.sort()
vlines.append(10**9)

yxs = collections.defaultdict(list)
ys = set()
for i in range(M):
    l, r, y = map(int, input().split())
    yxs[y].append((l, r))
    if l <= 1:
        ys.add(y)


def merge(segs):
    segs.sort()
    ans = [segs[0]]
    for s in segs[1:]:
        pre = ans[-1]
        if s[0] > pre[1]:
            # ans.append(s)
            return ans[0]
        else:
            ans[-1] = (pre[0], s[1])
    
    return ans[0]


xs = [merge(yxs[y])[1] for y in ys]
xs.sort()

ans = float('inf')
for i, x in enumerate(vlines):
    if i >= ans:
        break
    # count = i + sum([1 if u >= x else 0 for u in xs])
    count = i + len(xs) - bisect.bisect_left(xs, x)
    ans = min(ans, count)

print(ans)