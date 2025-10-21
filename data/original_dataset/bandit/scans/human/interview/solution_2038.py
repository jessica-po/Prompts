# from bisect import bisect_left

# (n) = (int(x) for x in input().split())
n = int(input())
a = [int(_) - 1 for _ in input().split()]

b = [0 for _ in a]
for id, v in enumerate(a):
    b[v] = id

ans = []
for i in range(n):
    pos = b[i]
    target = i
    old_v = a[target]
    if pos == target:
        continue

    # do swap
    b[old_v] = pos
    b[i] = i
    a[target] = i
    a[pos] = old_v


    if (abs(pos - target) * 2 >= n):
        ans.append((pos, target))
        continue
    elif max(pos, target) < n // 2:
        helper = n - 1
        ans.append((pos, helper))
        ans.append((target, helper))
        ans.append((pos, helper))
    elif min(pos, target) >= n // 2:
        helper = 0
        ans.append((pos, helper))
        ans.append((target, helper))
        ans.append((pos, helper))
    else:
        L = 0
        R = n - 1
        if pos > target:
            (pos, target) = (target, pos)
        ans.append((pos, R))
        ans.append((L, R))
        ans.append((L, target))
        ans.append((L, R))
        ans.append((pos, R))

print(len(ans))
for i in ans:
    print(i[0] + 1, i[1] + 1)