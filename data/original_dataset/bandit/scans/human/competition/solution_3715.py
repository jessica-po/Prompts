import sys

inp = sys.stdin
#inp = open('input.txt', 'r')

n = int(inp.readline())
a = list(map(int, inp.readline().split()))


best = [0, 0, 0]
for i in range(n):
    nx_best = [0, 0, 0]
    if a[i] in (1, 3):
        nx_best[1] = max(best[0], best[2]) + 1
    if a[i] in (2, 3):
        nx_best[2] = max(best[0], best[1]) + 1
    nx_best[0] = max(best)

    best = nx_best[:]

print(n - max(best))