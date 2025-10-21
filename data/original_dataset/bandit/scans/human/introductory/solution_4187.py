n = int(input())
a = list(map(int, input().split()))
b = []
for i in range(len(a)):
    b.append(a[i])
for i in range(len(a)):
    b.append(a[i])
q = 0
r = set()
for i in b:
    if i:
        q += 1
    else:
        r.add(q)
        q = 0
print(max(r))