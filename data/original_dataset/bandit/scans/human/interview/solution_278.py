import sys

n = int(input())
p = [int(i) for i in input().split()]
b = [int(i) for i in input().split()]

ans = 0
num_cycles = 0
checked = set()

for i in range(n):
    if i in checked:
        continue

    checked.add(i)

    nxt = p[i] - 1

    while nxt != i:
        checked.add(nxt)
        nxt = p[nxt] - 1

    num_cycles += 1

ans += num_cycles if num_cycles != 1 else 0
ans += (sum(b) % 2) == 0

print(ans)