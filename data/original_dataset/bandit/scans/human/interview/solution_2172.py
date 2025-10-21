n, m = map(int, input().split())
d = { }
for i in range(m):
    a, b = input().split()
    d[a] = b if len(b) < len(a) else a
for word in input().split():
    print(d[word], end=' ')
print()