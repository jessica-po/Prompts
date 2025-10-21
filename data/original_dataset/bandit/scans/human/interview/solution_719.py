from collections import defaultdict
k = int(input())

d = defaultdict(list)

for i in range(10):
    d[(1, i)].append(i)

mx = 10
pw = 1
for digs in range(2, mx):
    pw *= 10
    for sm in range(11):
        for curr in range(10):
            for num in d[(digs-1, sm-curr)]:
                d[(digs, sm)].append( curr*pw + num )

perfects = sorted(d[(mx-1, 10)])
#print(len(perfects))
print(perfects[k-1])