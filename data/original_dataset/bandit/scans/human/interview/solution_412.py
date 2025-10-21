n = int(input())
l = list(map(int, input().split()))
max1 = 1
for i in l:
    k = 1
    x = i
    while x % 2 == 0:
        k *= 2
        x //= 2
    max1 = max(max1, k)
c = 0
for i in l:
    if i % max1 == 0:
        c += 1
print(max1, c)