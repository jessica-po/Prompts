n, k = list(map(int, input().split()))
a = list(map(int, input().split()))
b = list(map(int, input().split()))
k1 = 0
k2 = 0
for x in a:
    if x % 2 == 0:
        k1 += 1
    else:
        k2 += 1
m1 = 0
m2 = 0
for x in b:
    if x % 2 == 0:
        m1 += 1
    else:
        m2 += 1
print(min(k1, m2) + min(k2, m1))