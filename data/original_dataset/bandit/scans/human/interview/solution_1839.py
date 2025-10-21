n = int(input())
h = [False] * n
v = [False] * n
result = [ ]
for i in range(n * n):
    a, b = list(map(int, input().split()))
    a -= 1
    b -= 1
    if not h[a] and not v[b]:
        h[a] = v[b] = True
        result.append(i + 1)
print(' '.join(map(str, result)))