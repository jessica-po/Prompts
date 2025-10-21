n = int(input())

from collections import defaultdict

first = defaultdict(int)
second = defaultdict(int)
for _ in range(n):
    s = input().strip()
    count = 0
    min_count = 0
    for c in s:
        if c == '(': count += 1
        else: count -= 1
        min_count = min(count, min_count)
    if min_count >= 0: first[count] += 1
    if count == min_count: second[count] += 1

res = 0
for k, v in list(first.items()):
    res += v * second[-k]

print(res)