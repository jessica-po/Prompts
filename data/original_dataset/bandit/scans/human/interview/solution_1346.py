from random import randint
import sys

n, m, p = list(map(int, input().strip().split()))

f = list(map(int, input().strip().split()))
g = list(map(int, input().strip().split()))

for i in range(len(f)):
    if f[i] % p != 0:
        break

j = 0
while g[j] % p == 0:
    j += 1

print(i+j)