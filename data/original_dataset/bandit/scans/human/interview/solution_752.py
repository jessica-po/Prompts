from collections import defaultdict
n = int(input())
d = defaultdict(int)
r = 0
for i in range(n):
    d[input()] += 1
for i in range(n):
    s = input()
    if d[s]:
        d[s] -= 1
    else:
        r += 1
print(r)