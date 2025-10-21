from collections import defaultdict


n, m = list(map(int, input().split()))

ns = list(map(int, input().split()))
ms = list(map(int, input().split()))
summs = sum(ms)

target = {
    i: m
    for i, m in enumerate(ms, 1)
}
remain = set(i for i, m in list(target.items()) if m != 0)

count = defaultdict(int)

a = 0
b = 0

while remain and b < n:
    count[ns[b]] += 1
    if ns[b] in remain and target[ns[b]] <= count[ns[b]]:
        remain.remove(ns[b])
    b += 1

if remain:
    print(-1)
else:
    ans = b - summs
    while b <= n:
        if remain:
            if b >= n:
                break
            count[ns[b]] += 1
            if ns[b] in remain and target[ns[b]] <= count[ns[b]]:
                remain.remove(ns[b])
            b += 1
        else:
            count[ns[a]] -= 1
            if target[ns[a]] > count[ns[a]]:
                remain.add(ns[a])
            else:
                ans = min(ans, b - a - 1 - summs)
            a += 1

    print(ans)