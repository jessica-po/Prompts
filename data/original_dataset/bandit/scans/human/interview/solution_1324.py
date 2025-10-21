s = 0
a = list(map(int, input().split()))
for i in map(int, input()):
    s += a[i - 1]
print(s)