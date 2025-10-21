n = int(input())
m = list(map(int, input().split()))
a = []
b = []
c = []
for i in range(n):
    if m[i] == 1:
        a.append(i + 1)
    if m[i] == 2:
        b.append(i + 1)
    if m[i] == 3:
        c.append(i + 1)
ans = min(len(a), len(b), len(c))
print(ans)
for i in range(ans):
    print(a[i], b[i], c[i])