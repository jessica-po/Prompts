import sys

def read_int():
    return int(input())

def read_ints():
    return [int(x) for x in input().split()]

n, d = read_ints()
a = read_ints()

a = sorted(a)

best = 0

for i in range(n):
    for j in range(i, n):
        if a[j] - a[i] <= d:
            best = max(best, j - i + 1)

print(len(a) - best)