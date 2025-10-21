n = int(input())

xs = [int(x) for x in input().split()]

pos = {}
for i, x in enumerate(xs):
    while x in pos:
        del pos[x]
        x *= 2
    pos[x] = i

ks = sorted(list(pos.keys()), key=lambda k: pos[k])

print(len(ks))
print(" ".join(map(str, ks)))