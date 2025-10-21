from collections import Counter
from itertools import accumulate
from math import sqrt
from operator import itemgetter
import sys
 
n = int(input())
cnt = Counter(map(int, input().split()))
nums, counts = zip(*sorted(cnt.items(), key=itemgetter(1)))
acc = [0] + list(accumulate(counts))
area = 1
h, w = 1, 1
i = len(counts)
 
for y in range(int(sqrt(n)), 0, -1):
    while i and counts[i-1] > y:
        i -= 1
    total = acc[i] + (len(counts) - i) * y
    x = total // y
    if y <= x and area < x * y:
        h, w, area = y, x, x*y
 
ans = [[0]*w for _ in range(h)]
i = len(counts)-1
num, count = nums[i], min(h, counts[i])
 
for x in range(w):
    for y in range(h):
        ans[y][(x + y) % w] = num
 
        count -= 1
        if count == 0:
            i -= 1
            num, count = nums[i], h if h < counts[i] else counts[i]
 
print(area)
print(h, w)
for y in range(h):
    sys.stdout.write(' '.join(map(str, ans[y])) + '\n')