import sys

n, z = list(map(int, sys.stdin.readline().strip().split()))
x = list(map(int, sys.stdin.readline().strip().split()))
x.sort()

i = 0
j = n // 2
c = 0
while j < n and i < n // 2:
    if x[j] - x[i] >= z:
        i = i + 1
        j = j + 1
        c = c + 1
    else:
        j = j + 1

print(c)