import sys

n, k = list(map(int, input().split()))
a = [int(x) for x in input().split()]
b = [int(x) for x in input().split()]

b.sort(reverse=True)

res = []
cur_b = 0
for a_i in a:
    if a_i != 0:
        res.append(a_i)
    else:
        res.append(b[cur_b])
        cur_b += 1

if res != list(sorted(res)):
    print("Yes")
else:
    print("No")