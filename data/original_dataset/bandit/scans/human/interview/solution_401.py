n, m = map(int, input().split())
a = [int(i) for i in input().split()]
b = [int(i) for i in input().split()]
a.sort()
b.sort()
for i in a:
    if i in b:
        print(i)
        break
else:
    print(min(a[0], b[0]), max(a[0], b[0]), sep = '')