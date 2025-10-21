import sys

n = int(sys.stdin.readline())
l = [int(x) for x in sys.stdin.readline().split(' ')]

ind = sorted(list(range(len(l))), key=lambda x: l[x])
h = l[ind[0]] - 1
for i in ind:
    if l[i] <= h:
        l[i] = h+1
        h += 1
    else:
        h = l[i]
print(" ".join([str(x) for x in l]))