n = int(input())
m = [int(i) for i in input().split()]

dm = [0 for i in range(n)]

dm[-1] = m[-1] + 1

for i in range(n - 2, -1, -1):
    dm[i] = max(m[i] + 1, m[i+1], dm[i+1]-1)
#print(dm)
for i in range(1, n):
    dm[i] = max(dm[i], dm[i-1])
#print(dm)

print(sum([dm[i] - 1 - m[i] for i in range(n)]))