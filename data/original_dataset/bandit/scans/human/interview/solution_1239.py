n = int(input())
a = [int(x) for x in input().split()]
a.sort()

diffs = [a[i] - a[i-1] for i in range(1, n)]
diffs.sort()

cur = 0
while cur < n - 1 and diffs[cur] == diffs[0]:
    cur += 1
print(diffs[0], cur)