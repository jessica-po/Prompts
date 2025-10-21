n = int(input())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
c = {}
for i in range(n):
    c[b[i]] = i
b = []
for i in range(n):
    a[i] = c[a[i]]
print(sum(abs(a[i] - i) for i in range(n)) >> 1)

while True:
    for i in range(n):
        if a[i] < i:
            for j in range(a[i], i):
                if a[j] >= i:
                    a[i], a[j] = a[j], a[i]
                    b += [(i+1, j+1)]
                    break
            break
    else:
        break

print(len(b))
for e in b:
    print(*e)