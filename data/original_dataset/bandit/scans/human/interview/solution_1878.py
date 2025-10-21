n = int(input())
r = 0
for i in range(n):
    a = list(map(int, input().split(' ')))
    r += (a[2] - a[0] + 1) * (a[3] - a[1] + 1)
print(r)