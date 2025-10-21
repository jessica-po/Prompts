n = int(input())

mas = list(map(int, input().split()))

dist = set([0])
res = 1
for i, e in enumerate(mas):
    time = i + 1
    if e in dist:
        dist.remove(e)
    else:
        res += 1
    dist.add(time)
print(res)