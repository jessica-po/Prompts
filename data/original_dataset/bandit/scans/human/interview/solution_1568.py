n, a, b, c, t = list(map(int, input().split()))

lst = []
for x in input().split():
    lst.append(int(x))

if b > c:
    print(n * a)
else:
    acc = 0
    for x in lst:
        acc += (t - x)
    acc *= (c - b)
    acc += n * a
    print(acc)