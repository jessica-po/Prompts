n = int(input())
a = list(map(int, input().split()))

o = []
cur = 0
for x in a:
    if x == 1:
        if cur > 0:
            o.append(cur)
        cur = 1
    else:
        cur += 1

o.append(cur)
print(len(o))
print(' '.join(str(x) for x in o))