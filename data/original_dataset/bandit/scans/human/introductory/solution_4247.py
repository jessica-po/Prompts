n = int(input())
p = list(map(int, input().split()))
s = 0
for i in range(n - 2):
    if p[i] < p[i + 1] < p[i + 2] or p[i] > p[i + 1] > p[i + 2]:
        s += 1
print(s)